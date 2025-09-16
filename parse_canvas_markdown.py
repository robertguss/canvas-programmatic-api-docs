import re
import json
from pathlib import Path
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from pydantic import BaseModel
import markdown
from bs4 import BeautifulSoup
from slugify import slugify
from genson import SchemaBuilder


@dataclass
class Parameter:
    name: str
    location: str  # 'path', 'query', 'body'
    type: str
    description: str
    required: bool = False
    enum_values: Optional[List[str]] = None


@dataclass
class Endpoint:
    method: str
    path: str
    name: str
    description: str
    scope: Optional[str] = None
    parameters: List[Parameter] = field(default_factory=list)
    response_schema: Optional[Dict[str, Any]] = None
    request_schema: Optional[Dict[str, Any]] = None


@dataclass
class Resource:
    name: str
    description: str
    endpoints: List[Endpoint] = field(default_factory=list)
    schemas: Dict[str, Dict[str, Any]] = field(default_factory=dict)


class CanvasMarkdownParser:
    ENDPOINT_PATTERN = re.compile(r'\*\*`(GET|POST|PUT|DELETE|PATCH)\s+([^`]+)`\*\*')
    SCOPE_PATTERN = re.compile(r'\*\*Scope:\*\*\s+`([^`]+)`')
    PATH_PARAM_PATTERN = re.compile(r':(\w+)')
    JSON_BLOCK_PATTERN = re.compile(r'```js\n(.*?)\n```', re.DOTALL)
    OBJECT_DEFINITION_PATTERN = re.compile(r'\*\*An? (\w+) object looks like:\*\*')
    
    def __init__(self):
        self.md = markdown.Markdown(extensions=['tables'])
    
    def parse_file(self, file_path: Path) -> Resource:
        content = file_path.read_text(encoding='utf-8')
        
        # Extract resource name from first heading
        resource_name = self._extract_resource_name(content)
        resource_description = self._extract_resource_description(content)
        
        # Extract schemas from JSON examples
        schemas = self._extract_schemas(content)
        
        # Find all endpoints
        endpoints = []
        for match in self.ENDPOINT_PATTERN.finditer(content):
            endpoint = self._parse_endpoint(content, match, schemas)
            if endpoint:
                endpoints.append(endpoint)
        
        return Resource(
            name=resource_name,
            description=resource_description,
            endpoints=endpoints,
            schemas=schemas
        )
    
    def _extract_resource_name(self, content: str) -> str:
        lines = content.split('\n')
        for line in lines:
            if line.startswith('# '):
                return line[2:].strip()
        return "Unknown Resource"
    
    def _extract_resource_description(self, content: str) -> str:
        lines = content.split('\n')
        in_description = False
        description_lines = []
        
        for line in lines:
            if line.startswith('## ') and 'API' in line:
                in_description = True
                continue
            elif in_description:
                if line.startswith('#') or line.startswith('**'):
                    break
                if line.strip():
                    description_lines.append(line.strip())
        
        return ' '.join(description_lines) if description_lines else ""
    
    def _extract_schemas(self, content: str) -> Dict[str, Dict[str, Any]]:
        schemas = {}
        
        # Find object definitions and their corresponding JSON examples
        lines = content.split('\n')
        current_object = None
        
        for i, line in enumerate(lines):
            # Look for object definition patterns
            obj_match = self.OBJECT_DEFINITION_PATTERN.search(line)
            if obj_match:
                current_object = obj_match.group(1)
                
                # Look for the next JSON block after this definition
                remaining_content = '\n'.join(lines[i:])
                json_match = self.JSON_BLOCK_PATTERN.search(remaining_content)
                
                if json_match:
                    json_str = json_match.group(1)
                    try:
                        # Clean up the JSON (remove comments)
                        cleaned_json = self._clean_json_comments(json_str)
                        json_obj = json.loads(cleaned_json)
                        
                        # Generate JSON schema from the example
                        builder = SchemaBuilder()
                        builder.add_object(json_obj)
                        schema = builder.to_schema()
                        
                        schemas[current_object] = schema
                    except (json.JSONDecodeError, Exception) as e:
                        print(f"Warning: Could not parse JSON for {current_object}: {e}")
                        continue
        
        return schemas
    
    def _clean_json_comments(self, json_str: str) -> str:
        # Remove JavaScript-style comments from JSON
        lines = json_str.split('\n')
        cleaned_lines = []
        
        for line in lines:
            # Remove inline comments (// comment)
            if '//' in line:
                # Find the comment, but be careful about URLs
                comment_pos = line.find('//')
                # Check if it's actually a comment and not part of a URL
                if comment_pos > 0 and line[comment_pos-1] not in [':', '"']:
                    line = line[:comment_pos].rstrip()
                elif comment_pos == 0 or (comment_pos > 0 and line[comment_pos-1] in [' ', '\t']):
                    line = line[:comment_pos].rstrip()
            
            if line.strip():
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def _parse_endpoint(self, content: str, match: re.Match, schemas: Dict[str, Dict[str, Any]] = None) -> Optional[Endpoint]:
        method = match.group(1)
        path = match.group(2).strip()
        
        # Find the content block for this endpoint
        start_pos = match.end()
        next_match = self.ENDPOINT_PATTERN.search(content, start_pos)
        end_pos = next_match.start() if next_match else len(content)
        
        endpoint_content = content[start_pos:end_pos]
        
        # Extract scope
        scope_match = self.SCOPE_PATTERN.search(endpoint_content)
        scope = scope_match.group(1) if scope_match else None
        
        # Extract description (first paragraph after the endpoint)
        description = self._extract_endpoint_description(endpoint_content)
        
        # Generate endpoint name
        name = self._generate_endpoint_name(method, path, description)
        
        # Extract parameters
        parameters = self._extract_parameters(endpoint_content, path, method)
        
        # Determine response schema based on endpoint description and available schemas
        response_schema = self._determine_response_schema(endpoint_content, schemas or {})
        
        return Endpoint(
            method=method,
            path=path,
            name=name,
            description=description,
            scope=scope,
            parameters=parameters,
            response_schema=response_schema
        )
    
    def _extract_endpoint_description(self, content: str) -> str:
        lines = content.split('\n')
        description_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith('**Scope:**'):
                continue
            if line.startswith('**Request Parameters:**'):
                break
            if line.startswith('**') or line.startswith('|'):
                break
            description_lines.append(line)
        
        return ' '.join(description_lines).strip()
    
    def _generate_endpoint_name(self, method: str, path: str, description: str) -> str:
        # Try to create a meaningful name from the path and description
        path_parts = [part for part in path.split('/') if part and not part.startswith(':')]
        
        if len(path_parts) >= 3:  # /api/v1/resource
            resource = path_parts[2]
            if len(path_parts) > 3:
                action = path_parts[-1]
                return f"{method} {resource} {action}".title()
            else:
                action_map = {
                    'GET': 'List',
                    'POST': 'Create',
                    'PUT': 'Update',
                    'DELETE': 'Delete',
                    'PATCH': 'Update'
                }
                return f"{action_map.get(method, method)} {resource}".title()
        
        # Fallback to method + simplified path
        simplified_path = path.replace('/api/v1/', '').replace(':', '')
        return f"{method} {simplified_path}".title()
    
    def _extract_parameters(self, content: str, path: str, method: str) -> List[Parameter]:
        parameters = []
        
        # Find path parameters
        path_params = self.PATH_PARAM_PATTERN.findall(path)
        for param_name in path_params:
            parameters.append(Parameter(
                name=param_name,
                location='path',
                type='string',
                description=f'The {param_name} identifier',
                required=True
            ))
        
        # Parse parameter table if it exists
        table_params = self._parse_parameter_table(content, method)
        parameters.extend(table_params)
        
        return parameters
    
    def _parse_parameter_table(self, content: str, method: str) -> List[Parameter]:
        parameters = []
        
        # Look for the parameter table section
        if '**Request Parameters:**' not in content:
            return parameters
        
        # Convert markdown to HTML for easier parsing
        html = self.md.convert(content)
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find the first table after "Request Parameters"
        tables = soup.find_all('table')
        if not tables:
            return parameters
        
        table = tables[0]
        rows = table.find_all('tr')
        
        if len(rows) < 2:  # Need header + at least one data row
            return parameters
        
        # Parse table rows (skip header)
        for row in rows[1:]:
            cells = row.find_all(['td', 'th'])
            if len(cells) >= 3:
                param_name = cells[0].get_text().strip().strip('`')
                param_type = cells[1].get_text().strip().strip('`')
                param_desc = cells[2].get_text().strip()
                
                # Determine parameter location
                location = 'query'  # default
                if method in ['POST', 'PUT', 'PATCH'] and param_type not in ['string', 'integer', 'boolean']:
                    location = 'body'
                
                # Check if required
                required = 'required' in param_desc.lower() or param_name.endswith('*')
                
                parameters.append(Parameter(
                    name=param_name.rstrip('*'),
                    location=location,
                    type=param_type,
                    description=param_desc,
                    required=required
                ))
        
        return parameters
    
    def _determine_response_schema(self, endpoint_content: str, schemas: Dict[str, Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        # Look for "Returns a list of [ObjectName]" or "Returns an [ObjectName]" patterns
        returns_pattern = re.compile(r'Returns (?:a list of |an? )?(?:\[([^\]]+)\]|\*\*([^*]+)\*\*|([A-Z][a-zA-Z]+))')
        
        match = returns_pattern.search(endpoint_content)
        if match:
            # Get the object name from any of the capture groups
            object_name = match.group(1) or match.group(2) or match.group(3)
            
            if object_name in schemas:
                schema = schemas[object_name].copy()
                
                # If it's a list, wrap in array schema
                if 'list of' in endpoint_content.lower():
                    return {
                        "type": "array",
                        "items": schema
                    }
                else:
                    return schema
        
        return None


def parse_all_resources(resources_dir: Path) -> Dict[str, Resource]:
    parser = CanvasMarkdownParser()
    resources = {}
    
    for md_file in resources_dir.glob('*.md'):
        try:
            resource = parser.parse_file(md_file)
            resources[md_file.stem] = resource
        except Exception as e:
            print(f"Error parsing {md_file.name}: {e}")
            continue
    
    return resources


if __name__ == "__main__":
    resources_dir = Path("data/canvas_api_resources")
    resources = parse_all_resources(resources_dir)
    
    print(f"Parsed {len(resources)} resources:")
    for name, resource in resources.items():
        print(f"  {resource.name}: {len(resource.endpoints)} endpoints")

import re
import json
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from pydantic import BaseModel
import markdown
from bs4 import BeautifulSoup
from slugify import slugify


@dataclass
class Parameter:
    name: str
    location: str  # 'path', 'query', 'body'
    type: str
    description: str
    required: bool = False


@dataclass
class Endpoint:
    method: str
    path: str
    name: str
    description: str
    scope: Optional[str] = None
    parameters: List[Parameter] = field(default_factory=list)


@dataclass
class Resource:
    name: str
    description: str
    endpoints: List[Endpoint] = field(default_factory=list)


class CanvasMarkdownParser:
    ENDPOINT_PATTERN = re.compile(r'\*\*`(GET|POST|PUT|DELETE|PATCH)\s+([^`]+)`\*\*')
    SCOPE_PATTERN = re.compile(r'\*\*Scope:\*\*\s+`([^`]+)`')
    PATH_PARAM_PATTERN = re.compile(r':(\w+)')
    
    def __init__(self):
        self.md = markdown.Markdown(extensions=['tables'])
    
    def parse_file(self, file_path: Path) -> Resource:
        content = file_path.read_text(encoding='utf-8')
        
        # Extract resource name from first heading
        resource_name = self._extract_resource_name(content)
        resource_description = self._extract_resource_description(content)
        
        # Find all endpoints
        endpoints = []
        for match in self.ENDPOINT_PATTERN.finditer(content):
            endpoint = self._parse_endpoint(content, match)
            if endpoint:
                endpoints.append(endpoint)
        
        return Resource(
            name=resource_name,
            description=resource_description,
            endpoints=endpoints
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
    
    def _parse_endpoint(self, content: str, match: re.Match) -> Optional[Endpoint]:
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
        
        return Endpoint(
            method=method,
            path=path,
            name=name,
            description=description,
            scope=scope,
            parameters=parameters
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

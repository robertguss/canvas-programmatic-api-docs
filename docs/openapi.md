# OpenAPI Specification Documentation

The Canvas LMS API OpenAPI specification provides a machine-readable description of the entire Canvas API. Generated automatically from the official Canvas API markdown documentation, it includes comprehensive endpoint definitions, parameter schemas, and response models.

## Overview

The OpenAPI specification is generated in two formats:
- `output/canvas_api.openapi.yaml` - YAML format (recommended)
- `output/canvas_api.openapi.json` - JSON format

### Specification Details

- **OpenAPI Version**: 3.1.0
- **API Version**: v1
- **Endpoints**: 1,018+ endpoints across 128 Canvas resources
- **Schemas**: 234+ data models with full validation
- **Authentication**: OAuth2 Bearer token support

## Generation Process

The OpenAPI specification is generated through a multi-step process:

1. **Markdown Parsing**: Extract endpoint information from Canvas API docs
2. **Schema Generation**: Create JSON schemas from example data in markdown
3. **OpenAPI Building**: Construct OpenAPI 3.1 compliant specification
4. **Validation**: Ensure specification meets OpenAPI standards

```bash
# Generate OpenAPI specification
just openapi

# Or run directly
python generate_openapi.py
```

## Features

### Comprehensive Endpoint Coverage

Every Canvas API endpoint is documented with:
- HTTP method and path
- Parameter definitions (path, query, body)
- Response schemas
- OAuth scopes required
- Detailed descriptions

### Rich Schema Definitions

The specification includes detailed schemas for:
- Request parameters
- Request bodies
- Response objects
- Error responses

Example schema for a Course object:
```yaml
Course:
  type: object
  properties:
    id:
      type: integer
      description: The unique identifier for the course
    name:
      type: string
      description: The full name of the course
    course_code:
      type: string
      description: The course code
    workflow_state:
      type: string
      enum: [unpublished, available, completed, deleted]
    # ... additional properties
```

### Authentication Configuration

OAuth2 Bearer token authentication is properly configured:

```yaml
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: Canvas API access token
security:
  - BearerAuth: []
```

## Using the OpenAPI Specification

### API Documentation

Use the specification to generate interactive API documentation:

```bash
# Using Swagger UI
npx swagger-ui-serve output/canvas_api.openapi.yaml

# Using Redoc
npx redoc-cli serve output/canvas_api.openapi.yaml
```

### Code Generation

Generate client libraries in various programming languages:

```bash
# Generate JavaScript client
openapi-generator-cli generate \
  -i output/canvas_api.openapi.yaml \
  -g javascript \
  -o clients/javascript

# Generate Java client
openapi-generator-cli generate \
  -i output/canvas_api.openapi.yaml \
  -g java \
  -o clients/java

# Generate Go client
openapi-generator-cli generate \
  -i output/canvas_api.openapi.yaml \
  -g go \
  -o clients/go
```

### API Testing

Use the specification for automated API testing:

```bash
# Using Dredd
dredd output/canvas_api.openapi.yaml https://yourschool.instructure.com/api/v1

# Using Postman Newman
newman run output/canvas_api.openapi.yaml
```

### Mock Servers

Create mock servers for development:

```bash
# Using Prism
prism mock output/canvas_api.openapi.yaml

# Using OpenAPI Mock Server
openapi-mock-server output/canvas_api.openapi.yaml
```

## Specification Structure

### Info Section

```yaml
openapi: 3.1.0
info:
  title: Canvas LMS API
  description: Complete Canvas LMS API specification
  version: "1.0"
  contact:
    name: Canvas API Documentation
    url: https://canvas.instructure.com/doc/api/
servers:
  - url: https://{institution}.instructure.com/api/v1
    description: Canvas LMS API Server
    variables:
      institution:
        default: canvas
        description: Your Canvas institution subdomain
```

### Paths

Endpoints are organized by resource type:

```yaml
paths:
  /accounts:
    get:
      summary: List accounts
      operationId: listAccounts
      tags: [Accounts]
      parameters:
        - name: include
          in: query
          schema:
            type: array
            items:
              type: string
      responses:
        '200':
          description: List of accounts
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Account'
```

### Components

Reusable schemas, parameters, and responses:

```yaml
components:
  schemas:
    Account:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        # ... additional properties
    
    Course:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        # ... additional properties
  
  parameters:
    CourseId:
      name: course_id
      in: path
      required: true
      schema:
        type: integer
      description: The unique identifier for the course
```

## Validation and Quality

The generated specification is validated against OpenAPI 3.1 standards:

- **Schema Validation**: All schemas are valid JSON Schema Draft 2020-12
- **Reference Resolution**: All `$ref` references resolve correctly
- **Required Fields**: All required OpenAPI fields are present
- **Type Consistency**: Parameter and response types are consistent

### Validation Tools

```bash
# Validate with swagger-codegen
swagger-codegen-cli validate -i output/canvas_api.openapi.yaml

# Validate with openapi-generator
openapi-generator-cli validate -i output/canvas_api.openapi.yaml

# Validate with spectral
spectral lint output/canvas_api.openapi.yaml
```

## Customization

### Adding Custom Extensions

You can extend the specification with custom vendor extensions:

```python
# In canvas_openapi/builder.py
spec["x-custom-extension"] = {
    "generator": "canvas-api-postman-generator",
    "version": "1.0.0"
}
```

### Filtering Endpoints

Generate specifications for specific resource types:

```python
# Generate only course-related endpoints
python generate_openapi.py --include-tags courses,assignments,submissions
```

### Custom Schemas

Override or extend generated schemas:

```python
# Add custom validation rules
custom_schemas = {
    "Course": {
        "type": "object",
        "properties": {
            "id": {"type": "integer", "minimum": 1},
            "name": {"type": "string", "minLength": 1}
        }
    }
}
```

## Integration Examples

### With API Gateway

Use the specification to configure AWS API Gateway:

```bash
aws apigateway import-rest-api \
  --body fileb://output/canvas_api.openapi.yaml \
  --parameters endpointConfigurationTypes=REGIONAL
```

### With Kong Gateway

Configure Kong using the OpenAPI specification:

```bash
deck sync --state output/canvas_api.openapi.yaml
```

### With Kubernetes

Deploy API documentation using Kubernetes:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: canvas-api-docs
spec:
  replicas: 1
  selector:
    matchLabels:
      app: canvas-api-docs
  template:
    metadata:
      labels:
        app: canvas-api-docs
    spec:
      containers:
      - name: swagger-ui
        image: swaggerapi/swagger-ui
        ports:
        - containerPort: 8080
        env:
        - name: SWAGGER_JSON
          value: /app/canvas_api.openapi.yaml
        volumeMounts:
        - name: openapi-spec
          mountPath: /app
      volumes:
      - name: openapi-spec
        configMap:
          name: canvas-openapi-spec
```

## Troubleshooting

### Common Issues

1. **Invalid References**: Ensure all `$ref` paths are correct
2. **Schema Validation Errors**: Check that all schemas follow JSON Schema standards
3. **Missing Required Fields**: Verify all required OpenAPI fields are present
4. **Type Mismatches**: Ensure parameter and response types are consistent

### Debug Mode

Enable debug output during generation:

```bash
python generate_openapi.py --debug
```

### Validation Errors

Fix common validation errors:

```bash
# Check for circular references
spectral lint output/canvas_api.openapi.yaml --ruleset spectral:oas

# Validate against OpenAPI 3.1 schema
ajv validate -s openapi-3.1-schema.json -d output/canvas_api.openapi.yaml
```

## Best Practices

### 1. Keep Specifications Updated

Regenerate the specification regularly to stay current with Canvas API changes:

```bash
# Update workflow
just fetch-docs    # Get latest Canvas docs
just openapi       # Regenerate specification
```

### 2. Version Control

Track specification changes in version control:

```bash
git add output/canvas_api.openapi.yaml
git commit -m "Update OpenAPI specification"
```

### 3. Automated Validation

Include specification validation in CI/CD pipelines:

```yaml
# GitHub Actions example
- name: Validate OpenAPI Spec
  run: |
    npm install -g @apidevtools/swagger-cli
    swagger-cli validate output/canvas_api.openapi.yaml
```

### 4. Documentation Generation

Automatically generate and deploy API documentation:

```bash
# Generate static documentation
redoc-cli build output/canvas_api.openapi.yaml --output docs/api.html
```

## Advanced Usage

### Custom Code Generation Templates

Create custom templates for code generation:

```bash
# Generate with custom templates
openapi-generator-cli generate \
  -i output/canvas_api.openapi.yaml \
  -g python \
  -t custom-templates/ \
  -o clients/python-custom
```

### Specification Merging

Combine with other API specifications:

```bash
# Merge multiple specifications
swagger-codegen-cli merge \
  -i output/canvas_api.openapi.yaml \
  -i other-api.openapi.yaml \
  -o merged-api.openapi.yaml
```

### Performance Optimization

Optimize specification size for large APIs:

```python
# Remove unused schemas
python optimize_openapi.py --remove-unused-schemas

# Compress specification
gzip output/canvas_api.openapi.yaml
```

The OpenAPI specification provides a solid foundation for API integration, documentation, and tooling across the Canvas LMS ecosystem.

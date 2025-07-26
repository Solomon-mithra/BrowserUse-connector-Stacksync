# Resume Task v1

This module allows you to resume execution of a previously paused task using the BrowserUse API.

## Endpoints
- **POST /execute**: Resume a paused task.

## Required Fields
- `api_connection`: API connection for BrowserUse
- `task_id`: ID of the task to resume

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "task_id": "task_1234567890abcdef"
}
```

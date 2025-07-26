# Stop Task v1

This module allows you to stop a running browser automation task immediately using the BrowserUse API.

## Endpoints
- **POST /execute**: Stop a running task.

## Required Fields
- `api_connection`: API connection for BrowserUse
- `task_id`: ID of the task to stop

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "task_id": "task_1234567890abcdef"
}
```

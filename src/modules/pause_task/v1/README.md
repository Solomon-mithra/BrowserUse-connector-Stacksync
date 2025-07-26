# Pause Task v1

This module allows you to pause execution of a running task using the BrowserUse API.

## Endpoints
- **POST /execute**: Pause a running task.

## Required Fields
- `api_connection`: API connection for BrowserUse
- `task_id`: ID of the task to pause

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "task_id": "task_1234567890abcdef"
}
```

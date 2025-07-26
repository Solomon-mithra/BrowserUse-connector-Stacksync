# Resume Task Module

This module resumes execution of a previously paused task. The task will continue from where it was paused.

## Endpoints
- **POST /execute**: Resume a paused task. Requires `api_connection` and `task_id` in the request body.

## Fields
- **api_connection** (connection, required): API connection for BrowserUse
- **task_id** (string, required): ID of the task to resume

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "task_id": "task_1234567890abcdef"
}
```

# Pause Task Module

This module pauses execution of a running task. The task can be resumed later using the /resume-task endpoint.

## Endpoints
- **POST /execute**: Pause a running task. Requires `api_connection` and `task_id` in the request body.

## Fields
- **api_connection** (connection, required): API connection for BrowserUse
- **task_id** (string, required): ID of the task to pause

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "task_id": "task_1234567890abcdef"
}
```

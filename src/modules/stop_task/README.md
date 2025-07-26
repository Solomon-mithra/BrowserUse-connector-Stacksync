# Stop Task Module

This module stops a running browser automation task immediately. The task cannot be resumed after being stopped.

## Endpoints
- **POST /execute**: Stop a running task. Requires `api_connection` and `task_id` in the request body.

## Fields
- **api_connection** (connection, required): API connection for BrowserUse
- **task_id** (string, required): ID of the task to stop

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "task_id": "task_1234567890abcdef"
}
```

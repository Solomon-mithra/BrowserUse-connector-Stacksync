# get_task_status Module

## Purpose
Get the current status of a Browser Use task. Returns only the status (created, running, finished, stopped, paused, or failed).

## Endpoints
- `/execute` (POST): Returns status for a given `task_id`.

## Fields
- **api_connection**: API connection to Browser Use.
- **task_id**: ID of the task to check status for.

## Example Request
```
{
  "api_connection": { ... },
  "task_id": "abc123"
}
```

## Example Response
```
{
  "data": { "status": "running" },
  "metadata": { "processed_at": "2024-01-01T00:00:00Z" }
}
```

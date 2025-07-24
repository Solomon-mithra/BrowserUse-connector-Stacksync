# Get Task Screenshots Module

## Purpose
Get screenshots generated during task execution. Returns screenshot URLs captured at key moments.

## Endpoints
- `/execute` (POST): Returns screenshot URLs for a given `task_id`.

## Fields
- **api_connection**: API connection to Browser Use.
- **task_id**: ID of the task to get screenshots for.

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
  "data": { "screenshots": ["https://...", "https://..."] },
  "metadata": { "processed_at": "2024-01-01T00:00:00Z" }
}
```

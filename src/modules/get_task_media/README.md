# Get Task Media Module

## Purpose
Get media files generated during task execution. Returns links to recordings or media generated during the process. Only available for completed tasks.

## Endpoints
- `/execute` (POST): Returns media links for a given `task_id`.

## Fields
- **api_connection**: API connection to Browser Use.
- **task_id**: ID of the task to get media for.

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
  "data": { "media": ["https://...", "https://..."] },
  "metadata": { "processed_at": "2024-01-01T00:00:00Z" }
}
```

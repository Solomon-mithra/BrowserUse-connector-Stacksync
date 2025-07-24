# Get Task GIF Module

## Purpose
Get an animated GIF of the task execution. Returns a GIF URL generated from screenshots. Only available for completed tasks with screenshots.

## Endpoints
- `/execute` (POST): Returns GIF URL for a given `task_id`.

## Fields
- **api_connection**: API connection to Browser Use.
- **task_id**: ID of the task to get GIF for.

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
  "data": { "gif_url": "https://...gif" },
  "metadata": { "processed_at": "2024-01-01T00:00:00Z" }
}
```

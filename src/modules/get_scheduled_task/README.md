# Get Scheduled Task Module

## Purpose
Get detailed information about a specific scheduled task, including its schedule configuration and current status.

## Endpoints
- `/execute` (POST): Returns details for a given scheduled task ID.

## Fields
- **api_connection**: API connection to Browser Use.
- **task_id**: ID of the scheduled task to retrieve.

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
  "data": { ...scheduled task info... },
  "metadata": { "processed_at": "2024-01-01T00:00:00Z" }
}
```

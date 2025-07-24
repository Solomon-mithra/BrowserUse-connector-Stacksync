# List Scheduled Tasks Module

## Purpose
Get a paginated list of all scheduled tasks for the user, ordered by creation date. Each task includes basic info like schedule type, next run time, and status.

## Endpoints
- `/execute` (POST): Returns a paginated list of scheduled tasks for the user.

## Fields
- **api_connection**: API connection to Browser Use.
- **page**: Page number (default: 1).
- **limit**: Items per page (default: 10).

## Example Request
```
{
  "api_connection": { ... },
  "page": 1,
  "limit": 10
}
```

## Example Response
```
{
  "data": { "scheduled_tasks": [ ... ] },
  "metadata": { "processed_at": "2024-01-01T00:00:00Z" }
}
```

# List Tasks Module

## Purpose
Get a paginated list of all tasks for the user, ordered by creation date. Each task includes basic info like status and creation time.

## Endpoints
- `/execute` (POST): Returns a paginated list of tasks for the user.

## Fields
- **api_connection**: API connection to Browser Use.

## Example Request
```
{
  "api_connection": { ... }
}
```

## Example Response
```
{
  "data": { "tasks": [ ... ] },
  "metadata": { "processed_at": "2024-01-01T00:00:00Z" }
}
```

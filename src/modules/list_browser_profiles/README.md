# List Browser Profiles Module

This module returns a paginated list of all browser profiles belonging to the user, ordered by creation date.

## Endpoints
- **POST /execute**: List browser profiles. Requires `api_connection`. Optional: `page`, `limit`.

## Fields
- **api_connection** (connection, required): API connection for BrowserUse
- **page** (integer, optional): Page number (default: 1)
- **limit** (integer, optional): Number of items per page (default: 10)

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "page": 1,
  "limit": 10
}
```

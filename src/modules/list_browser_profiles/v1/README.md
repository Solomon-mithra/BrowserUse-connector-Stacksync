# List Browser Profiles v1

This module allows you to list all browser profiles for the user using the BrowserUse API.

## Endpoints
- **POST /execute**: List browser profiles.

## Required Fields
- `api_connection`: API connection for BrowserUse

## Optional Fields
- `page`: Page number (default: 1)
- `limit`: Number of items per page (default: 10)

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "page": 1,
  "limit": 10
}
```

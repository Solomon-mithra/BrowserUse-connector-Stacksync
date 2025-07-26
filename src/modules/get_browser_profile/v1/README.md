# Get Browser Profile v1

This module allows you to get information about a specific browser profile using the BrowserUse API.

## Endpoints
- **POST /execute**: Get browser profile info.

## Required Fields
- `api_connection`: API connection for BrowserUse
- `profile_id`: ID of the browser profile to retrieve

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "profile_id": "profile_1234567890abcdef"
}
```

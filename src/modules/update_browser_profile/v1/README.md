# Update Browser Profile v1

This module allows you to update a browser profile with partial updates using the BrowserUse API.

## Endpoints
- **POST /execute**: Update browser profile.

## Required Fields
- `api_connection`: API connection for BrowserUse
- `profile_id`: ID of the browser profile to update

## Optional Fields
- `profile_name`: Name of the browser profile
- `description`: Description of the profile
- `persist`: Save cookies, local storage, and session data between tasks
- `ad_blocker`: Block ads and popups during automated tasks
- `proxy`: Route traffic through mobile proxies for better stealth
- `proxy_country_code`: Country code for the proxy
- `browser_viewport_width`: Browser viewport width in pixels
- `browser_viewport_height`: Browser viewport height in pixels

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "profile_id": "profile_1234567890abcdef",
  "profile_name": "Updated Name"
}
```

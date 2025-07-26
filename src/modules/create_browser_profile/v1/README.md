# Create Browser Profile v1

This module allows you to create a new browser profile with custom settings for ad blocking, proxy usage, and viewport dimensions using the BrowserUse API.

## Endpoints
- **POST /execute**: Create a new browser profile.

## Required Fields
- `api_connection`: API connection for BrowserUse
- `profile_name`: Name of the browser profile

## Optional Fields
- `description`: Description of the profile
- `persist`: Save cookies, local storage, and session data between tasks (default: true)
- `ad_blocker`: Block ads and popups during automated tasks (default: true)
- `proxy`: Route traffic through mobile proxies for better stealth (default: true)
- `proxy_country_code`: Country code for the proxy (default: US)
- `browser_viewport_width`: Browser viewport width in pixels (default: 1280)
- `browser_viewport_height`: Browser viewport height in pixels (default: 960)

## Example Request
```
POST /execute
{
  "api_connection": { ... },
  "profile_name": "My Profile",
  "description": "Test profile",
  "persist": true,
  "ad_blocker": true,
  "proxy": true,
  "proxy_country_code": "US",
  "browser_viewport_width": 1280,
  "browser_viewport_height": 960
}
```

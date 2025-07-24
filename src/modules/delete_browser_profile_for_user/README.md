# Reset Browser Profile

Deletes the browser profile for the user. This is useful when you want to start with a fresh browser state, clearing all stored cookies, sessions, and browser data.

## Endpoints
- `POST /api/v1/delete-browser-profile-for-user`

## Fields
- `api_connection`: API connection to Browser Use account.
- `user_id`: ID of the user whose browser profile will be reset.

## Example Usage
Send a POST request with the required fields to reset the browser profile for a user.

# Copilot Instructions for Stacksync App Connector Template (with Concrete Best Practices)

## Project Architecture
- This repo is a template for building Stacksync workflow connectors as Python microservices.
- Main entrypoint: `main.py` (registers Flask routes, loads modules).
- Modules live in `src/modules/{module_name}/{version}/` and include:
  - `route.py` (Flask endpoints)
  - `schema.json` (UI/data schema)
  - `module_config.yaml` (metadata)
  - `README.md` (module docs)
- Each module exposes `/execute`, `/content`, and optionally `/schema` endpoints for workflow integration.

## Developer Workflow
- Use `run_dev.sh` (Mac/Linux) or `run_dev.bat` (Windows) to start the dev server at `http://localhost:2003`.
- Build/rebuild with `./run_dev.sh --build` if dependencies or Docker config change.
- Add Python dependencies to `requirements.txt`.
- For new modules, copy `src/modules/new_empty_action/` and update names/configs.
- Edit `app_config.yaml` for connector-wide settings.

## Schema & Endpoint Patterns
- **Module schemas (`schema.json`)** define UI fields, validation, and UI order for workflow actions. Always keep schema and endpoint logic tightly synchronized.
- **Supported field types:**
  - `string`: For text, IDs, names, etc.
  - `boolean`: For true/false options.
  - `integer`: For numbers, counts, intervals.
  - `array`: For lists, multi-selects, managed arrays.
  - `object`: For structured data, advanced config.
- **Special field types:**
  - For JSON/code input, use `CodeblockWidget` with `{ "ui_options": { "widget": "CodeblockWidget", "language": "json" } }`.
  - For dropdowns or choices, use `enum` and optionally `/content` endpoint for dynamic options.
- **Schema best practices:**
  - Use `title` and `description` for every field for clear UI labels and help texts.
  - Use `required` array for mandatory fields.
  - Use `ui.order` to control field order in the UI.
  - Use `ui.help` for field-level help text.
  - For managed arrays, use `items` with type and UI options.
  - For advanced validation, use `pattern`, `minimum`, `maximum`, etc.
- **Endpoint conventions:**
  - `/execute`: Main action endpoint. Accepts only fields defined in schema. Returns `Response(data=..., metadata=...)`.
  - `/content`: For dynamic dropdowns or managed arrays (optional).
  - `/schema`: Returns the module's schema (optional, POST).
  - Always validate required fields and return clear error messages.
  - For mock responses, return all relevant fields and metadata for UI testing.
  - For real API calls, use `requests` and handle errors gracefully.

## Integration & Conventions
- External API calls: use `requests` in `route.py`.
- Response format: always use `Response(data=..., metadata=...)` from `workflows_cdk`.
- Secrets: pass as JSON string or object, encrypted before storage.
- Dynamic content: implement `/content` endpoint for managed dropdowns, etc.
- Use `module_config.yaml` to declare module metadata and versioning.

## Key Files & References
- `main.py`: App entrypoint, router setup.
- `src/modules/create_contacts/`: Example of all patterns.
- `documentation/how-to-build-a-module-schema.md`: Step-by-step schema guide.
- `config/Dockerfile.dev`, `run_dev.sh`: Dev environment setup.

## Template Generation Best Practices
- When given a set of parameters/fields, always:
  1. Create a module directory: `src/modules/{module_name}/v1/`
  2. Add `route.py` with `/execute` and `/schema` endpoints.
  3. Add `schema.json` with all fields, types, UI order, help, and validation.
  4. Add `module_config.yaml` with name, version, description, author.
  5. Add `README.md` with endpoint usage and field descriptions.
- Use the above schema and endpoint conventions for every new module.
- For any new field type or UI pattern, update this file with the concrete example.

## Tips
- Keep schema and endpoint logic tightly synchronized.
- Use descriptive field labels and help texts in schemas.
- Prefer explicit field types and validation for robust UI/UX.
- For advanced patterns, see `/documentation` and Stacksync docs.

---

If any conventions or workflows are unclear, please request clarification or examples from the user.

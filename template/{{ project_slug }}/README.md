# {{ project_name }}

{% if project_description %}{{ project_description }}{% else %}Project description goes here.{% endif %}

## Getting Started

### Stack Preset
{% if stack_preset == "django" %}
- Preset: Django (Python)
- Tooling: {{ python_tooling }}
  - App entry: `app/manage.py`
  - Templates: `app/templates/`
  - Static: `app/static/`
{% elif stack_preset == "express-vue" %}
- Preset: Express + Vue (Node)
- Package manager: {{ node_package_manager }}
  - API: `api/`
  - Frontend: `frontend/`
{% else %}
- Preset: None (fill in your stack)
{% endif %}

### Environment
- A `.env` file is generated at project creation time based on your Copier answers.
- The JWT secret is generated locally during creation and never stored in the template.

### Docker (optional)
{% if use_docker %}
Bring the stack up:

```bash
docker compose up -d
```

Bring the stack down:

```bash
docker compose down
```
{% else %}
Docker is not enabled for this project.
{% endif %}

### Linting, Formatting, Testing
- Commands are wired through the `Makefile` targets:
- `make ci-setup`, `make lint`, `make format-check`, `make typecheck`, `make test`, `make build`
- Use `scripts/check.sh` to run the full local CI-style checks.

## Project Updates (Copier)
This project was generated with Copier. To update with template changes:

```bash
copier update
```

## Windows Notes
- Prefer PowerShell scripts in `scripts/` on Windows.
- If using Bash on Windows, ensure LF line endings for `.sh` files.

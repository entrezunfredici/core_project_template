# core_project_template

A minimal, language-agnostic Copier template for production-oriented projects. It includes optional Docker, CI placeholders, scripts, and docs to get teams moving quickly without locking into a specific stack.

## What this template generates

- `{{ project_slug }}` project directory under `template/`
- `.copier-answers.yml` for `copier update`
- Optional Docker baseline, CI configs, and pre-commit hooks

## Quickstart

Create a new project:

```bash
copier copy https://github.com/entrezunfredici/core_project_template mon-nouveau-projet
```

Update an existing project:

```bash
copier update https://github.com/entrezunfredici/core_project_template mon-nouveau-projet
```

## Notes

- This template is OS-agnostic and supports Windows + Linux.
- The generated README includes placeholders for lint/test and Docker steps.
- Scripts are provided in both POSIX and PowerShell flavors.

import argparse
import base64
import secrets
from pathlib import Path


def gen_jwt_secret(bits: int = 256) -> str:
    nbytes = bits // 8
    key_bytes = secrets.token_bytes(nbytes)
    return base64.urlsafe_b64encode(key_bytes).rstrip(b"=").decode("ascii")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a .env file for the project.")
    parser.add_argument("--stack", required=True, choices=["django", "express-vue", "none"])
    parser.add_argument("--include-postgres", default="False")
    parser.add_argument("--django-port", type=int, default=8000)
    parser.add_argument("--api-port", type=int, default=4000)
    parser.add_argument("--frontend-port", type=int, default=5173)
    args = parser.parse_args()

    include_postgres = str(args.include_postgres).lower() in {"1", "true", "yes"}
    env_lines = []

    env_lines.append(f"PROJECT_NAME={{ project_name }}")

    if args.stack == "django":
        env_lines.extend(
            [
                f"DJANGO_SECRET_KEY={secrets.token_urlsafe(50)}",
                "DJANGO_DEBUG=1",
                "DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1",
                f"DJANGO_PORT={args.django_port}",
            ]
        )
    elif args.stack == "express-vue":
        env_lines.extend(
            [
                "NODE_ENV=development",
                f"API_PORT={args.api_port}",
                f"FRONTEND_PORT={args.frontend_port}",
                f"VITE_API_URL=http://localhost:{args.api_port}",
            ]
        )

    if args.stack != "none":
        env_lines.append(f"AUTH_JWT_SECRET={gen_jwt_secret()}")

    if include_postgres:
        env_lines.extend(
            [
                "POSTGRES_DB=app",
                "POSTGRES_USER=postgres",
                "POSTGRES_PASSWORD=postgres",
                "POSTGRES_HOST=db",
                "POSTGRES_PORT=5432",
            ]
        )

    env_path = Path(".env")
    env_path.write_text("\n".join(env_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

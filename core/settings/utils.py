from decouple import config

ALLOWED_ENVIRONMENTS = [
    "dev",
    "homol",
    "prod",
]


def get_settings_module() -> str:
    environment = config("ENV")

    if environment not in ALLOWED_ENVIRONMENTS:
        raise Exception(f"{environment} is not a valid environment.")

    return f"core.settings.{environment}"

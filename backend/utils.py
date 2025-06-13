from dotenv import load_dotenv
import os

def load_dotenvs():
    base_env_file = ".env"
    env_type_key = "ENVIRONMENT"

    if not load_dotenv(base_env_file):
        raise RuntimeError(f"Could not load base environment file: '{base_env_file}'")

    env_type = os.getenv(env_type_key)
    if not env_type:
        raise RuntimeError(f"Environment variable '{env_type_key}' is not set in '{base_env_file}'")

    custom_env_file = f"{base_env_file}.{env_type}"
    if not load_dotenv(custom_env_file, override=True):
        raise RuntimeError(f"Could not load environment-specific file: '{custom_env_file}'")

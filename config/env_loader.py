# config/env_loader.py

from pydantic_settings import BaseSettings
from pydantic import ValidationError
from pathlib import Path

class EnvHelperSettings(BaseSettings):
    class Config:
        extra = 'allow'  # Allows extra variables not explicitly defined

class EnvLoad:
    @classmethod
    def load_into_instance(cls, instance, env_file_path: str = None):
        """
        If env_file_path is provided, load from that .env file.
        Otherwise, load from system environment variables directly.
        """

        try:
            if env_file_path:
                # Resolve and check
                env_path = Path(env_file_path).resolve()
                if not env_path.exists():
                    raise FileNotFoundError(f".env file not found at: {env_path}")

                loaded_settings = EnvHelperSettings(_env_file=str(env_path)).model_dump()
            else:
                # No .env file; load directly from the system environment
                loaded_settings = EnvHelperSettings().model_dump()

            # Dynamically set these attributes on the instance
            for key, value in loaded_settings.items():
                setattr(instance, key, value)

        except ValidationError as e:
            raise EnvironmentError(
                f"Missing or invalid environment variables: {e.errors()}"
            )

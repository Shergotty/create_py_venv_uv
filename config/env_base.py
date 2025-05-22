# config/env_base.py

from config.env_loader import EnvLoad
from pathlib import Path
import importlib.util

class EnvBase:
    @classmethod
    def load_env_variables(cls, env_file_name: str = '.env'):
        """
        If env_file_name is None or empty, we won't use .env at all and
        just load system environment variables.
        """
        if env_file_name is None:
            # Load directly from the system environment
            EnvLoad.load_into_instance(cls, env_file_path=None)
            return

        # Otherwise, proceed to load from a .env file in the class's directory
        module_spec = importlib.util.find_spec(cls.__module__)
        if module_spec and module_spec.origin:
            env_file_path = Path(module_spec.origin).parent / env_file_name
            EnvLoad.load_into_instance(cls, env_file_path=str(env_file_path))
        else:
            raise FileNotFoundError(
                f"Could not determine the file path for module {cls.__module__}"
            )

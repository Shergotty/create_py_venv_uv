# env_service.py
from config.env_base import EnvBase

class EnvService(EnvBase):
    def __init__(self, use_env_file: bool = True):
        # If we don't want to load an .env file, pass None
        # Otherwise, we pass '.env' (or a custom name)
        env_file_name = '.env' if use_env_file else None
        self.load_env_variables(env_file_name=env_file_name)

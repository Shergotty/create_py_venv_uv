from env_service import EnvService

## Load from .env file:
# service = EnvService(use_env_file=True)

# OR load from system environment variables:
service = EnvService(use_env_file=False)
print (service)

import os
from dotenv import load_dotenv

load_dotenv()

class _EnvironmentVarLoader:
    def __init__(self):
        self._load_env()

    def _load_env(self):
        self._load_env_file('.env')

    def _load_env_file(self, env_file):
        load_dotenv(env_file)

    def get_env(self, env_name):
        return os.getenv(env_name)

    def get_env_or_raise(self, env_name):
        env_value = self.get_env(env_name)
        if env_value is None:
            raise Exception(f'Environment variable {env_name} not found')
        return env_value

EnvironmentVarLoader = _EnvironmentVarLoader()

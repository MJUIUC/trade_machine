from alpaca.data.historical import NewsClient
from alpaca.data.requests import NewsRequest
from trade_machine.environment_loader import EnvironmentVarLoader

api_key = EnvironmentVarLoader.get_env_or_raise('ALPACA_MARKETS_API_KEY')
api_secret = EnvironmentVarLoader.get_env_or_raise('ALPACA_MARKETS_API_SECRET')

class AlpacaMarketNewsClient:
    def __init__(self):
        self._client = NewsClient(api_key, api_secret)
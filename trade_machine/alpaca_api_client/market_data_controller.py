from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import (
    StockLatestQuoteRequest, 
    StockQuotesRequest,  
    StockLatestBarRequest, 
    StockBarsRequest,
    StockSnapshotRequest
)
from trade_machine.environment_loader import EnvironmentVarLoader

from datetime import datetime

api_key = EnvironmentVarLoader.get_env_or_raise('ALPACA_MARKETS_API_KEY')
secret_key = EnvironmentVarLoader.get_env_or_raise('ALPACA_MARKETS_API_SECRET')


class AlpacaMarketsHistoricalDataClient:
    def __init__(self):
        self._client = StockHistoricalDataClient(api_key, secret_key)

    def get_symbol_snapshot(self, symbol: str):
        return self.get_multiple_symbols_snapshot([symbol])

    def get_multiple_symbols_snapshot(self, symbols: list[str]):
        request = StockSnapshotRequest(symbol_or_symbols=symbols)
        return self._client.get_stock_snapshot(request)

    def get_multiple_symbols_historical_bars(self, symbols: list[str], start_date: datetime, end_date: datetime):
        historical_bars_request = StockBarsRequest(
            symbol_or_symbols=symbols,
            start_date=start_date,
            end_date=end_date
        )
        return self._client.get_stock_bars(historical_bars_request)

    def get_multiple_symbols_historical_quotes(self, symbols: list[str], start_date: datetime, end_date: datetime):
        historical_quotes_request = StockQuotesRequest(
            symbol_or_symbols=symbols,
            start_date=start_date,
            end_date=end_date
        )
        return self._client.get_stock_historical_quotes(historical_quotes_request)

    def get_multiple_symbols_latest_quotes(self, symbols: list[str]):
        latest_quote_request = StockLatestQuoteRequest(
            symbol_or_symbols=symbols)
        return self._client.get_stock_latest_quote(latest_quote_request)

    def get_multiple_symbols_latest_bars(self, symbols: list[str]):
        latest_bar_request = StockLatestBarRequest(symbol_or_symbols=symbols)
        return self._client.get_stock_latest_bar(latest_bar_request)

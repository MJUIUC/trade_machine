from fastapi import FastAPI
from trade_machine.alpaca_api_client.market_data_client import AlpacaMarketsHistoricalDataClient

http_service = FastAPI()
historical_data_client = AlpacaMarketsHistoricalDataClient()

@http_service.get("/")
async def root():
    test_dict = historical_data_client.get_symbol_snapshot('AAPL')
    return {"test": test_dict}

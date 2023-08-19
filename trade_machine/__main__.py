import uvicorn
from .http_service import http_service
from .database_connector import DbConnector

# Create the database tables
# If the tables already exist, this will do nothing
DbConnector.base.metadata.create_all(DbConnector.engine)

def main():
    uvicorn.run(http_service, host="127.0.0.1", port=8080, log_level="info")

def dev():
    uvicorn.run("trade_machine.http_service:http_service", host="127.0.0.1", port=8080, log_level="info", reload=True)

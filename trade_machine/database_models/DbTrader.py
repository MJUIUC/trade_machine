from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from trade_machine.database_connector import DatabaseConnector

"""
 This class is a database model for the trader table. It is used to store information about a trader using this application.
 Most of the fields will correspond to the account fields in the Alpaca API.
"""

class DbTrader(DatabaseConnector.Base):
    __tablename__ = 'trader'

    id = Column(Integer, primary_key=True)
    alpaca_id = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    created_at = Column(String, server_default=str(datetime.utcnow()))
    updated_at = Column(String, onupdate=str(datetime.utcnow()))
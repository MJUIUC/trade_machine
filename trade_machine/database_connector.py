from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class _SQLiteConnector:
    def __init__(self, db_path):
        self.engine = create_engine(f'sqlite:///{db_path}', connect_args={'check_same_thread': False})
        self.base = declarative_base()
        self.session = sessionmaker(bind=self.engine)()

    def __repr__(self) -> str:
        return f'<SQLiteConnector: {self.engine}>'

DbConnector = _SQLiteConnector('trade_machine.db')

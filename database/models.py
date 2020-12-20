from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class SearchHistory(Base):
    __tablename__ = 'search_history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    query_text = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

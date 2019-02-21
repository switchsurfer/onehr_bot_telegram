from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class media(Base):
    __tablename__ = 'mediaids'
    id = Column(Integer, primary_key=True)
    file_id = Column(String(255))
    filename = Column(String(255))

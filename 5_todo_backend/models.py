from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base



class Item(Base):
    __tablename__ = "todos"  # Renamed to plural for convention
    id = Column(Integer, primary_key=True, index=True)
    todo = Column(String, index=True)
   
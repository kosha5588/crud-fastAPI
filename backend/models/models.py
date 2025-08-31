from sqlalchemy import Boolean, Column, Integer, String
from backend.db.db import Base

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    completed = Column(Boolean, default=False)

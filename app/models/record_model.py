from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship

Base = declarative_base()

class Record(Base):
    __tablename__ = 'record'

    record_id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(UUID(as_uuid=True), nullable=False)
    media_id = Column(Text, nullable=False)
    media_type = Column(Text, nullable=False)
    status = Column(Text, nullable=False)
    progress = Column(Text, nullable=True)
    
    user = relationship("User", back_populates="records")

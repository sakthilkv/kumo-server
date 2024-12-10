from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from extension import db
import uuid

class Record(db.Model):
    __tablename__ = 'Record'

    record_id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(UUID(as_uuid=True), db.ForeignKey('User.uid'), nullable=False)
    media_id = Column(Text, nullable=False)
    media_type = Column(Text, nullable=False)
    status = Column(Text, nullable=False)
    progress = Column(Text, nullable=True)

    # Use 'User' as a string reference to avoid initialization issues
    user = db.relationship('User', backref=db.backref('Record', lazy=True))

    def __repr__(self):
        return f"<Record(record_id={self.record_id}, uid={self.uid}, media_id={self.media_id}, media_type={self.media_type}, status={self.status}, progress={self.progress})>"
    
    @classmethod
    def check_media_status(cls, uid,media_type,media_id):
        return db.session.query(Record).filter_by(uid=uid,media_type=media_type,media_id=str(media_id)).first()
    
    
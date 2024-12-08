import logging
from flask import jsonify
from extension import db
from app.models import Record

class RecordController:

    @staticmethod
    def add_record():
        pass
    
    @staticmethod
    def get_dashboard(uid,media_type):
        records = db.session.query(Record).filter_by(uid=uid,media_type=media_type).all()
        print("Found: ", len(records))
        response = {"results":[]}
        if records:
            for record in records:
                response["results"].append({
                    "record_id": record.record_id,
                    "uid": str(record.uid),
                    "media_id": record.media_id,
                    "media_type": record.media_type,
                    "status": record.status,
                    "progress": record.progress if record.progress else None,
                })
        return jsonify(response), 200   
        


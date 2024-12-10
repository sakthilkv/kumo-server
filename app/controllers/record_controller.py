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

    @staticmethod
    def add_media(uid,media_type,media_id,status):
        record = Record.check_media_status(uid=uid,media_type=media_type,media_id=media_id)
        if record:
            if status == "none":
                db.session.delete(record)
                db.session.commit()
                return jsonify({"message": "Record Deleted"}), 200
            elif record.status != status:
                record.status = status
                db.session.commit()
                return jsonify({"message": "Status Updated"}), 200
            
    
        else:
            try:
                new_record = Record(uid=uid,media_type=media_type,media_id=media_id,status=status)
                db.session.add(new_record)
                db.session.commit()
                return jsonify({"message":"Media Added"}), 200
            except Exception as e:
                print(e)
                return jsonify({"message":str(e)}), 500
        
        
        


from init import db, ma

class Attendance(db.Model):
    __tablename__ = 'attendance'

    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date)
    arrival_time = db.Column(db.Time)
    departure_time = db.Column(db.Time, nullable=False)
    status_id = db.Column(db.Integer, nullable=False)

class AttendanceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'child_id', 'date', 'arrival_time', 'departure_time', 'status_id')


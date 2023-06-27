from init import db, ma

class AttendanceStatus(db.Model):
    __tablename__ = 'attendance_statuses'

    id = db.Column(db.Integer, primary_key=True)
    status_name = db.Column(db.String(50), nullable=False)
    status_desc = db.Column(db.Text())

class AttendanceStatusSchema(ma.Schema):
    class Meta:
        fields = ('id', 'status_name', 'status_desc')

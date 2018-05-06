from app import db, login_manager


class Temperature(db.Model):
    __tablename__ = 'daq_temp'
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    channel = db.Column(db.String(5))
    value = db.Column(db.Float)

    def __repr__(self):
        return str(self.datetime)

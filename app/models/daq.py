from app import db, login_manager


class Temperature(db.Model):
    __tablename__ = 'daq_temp'
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    channel = db.Column(db.String(5))
    value = db.Column(db.Float)

    def __repr__(self):
        return str(self.datetime)


class Power(db.Model):
    __tablename__ = 'daq_power'
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.DateTime)
    voltage1 = db.Column(db.Float)
    current1 = db.Column(db.Float)
    voltage2 = db.Column(db.Float)
    current2 = db.Column(db.Float)
    voltage3 = db.Column(db.Float)
    current3 = db.Column(db.Float)
    voltage4 = db.Column(db.Float)
    current4 = db.Column(db.Float)

    def __repr__(self):
        return str(self.datetime)

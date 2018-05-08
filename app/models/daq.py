from app import db, login_manager


class Project(db.Model):
    __tablename__ = 'daq_project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return str(self.name)


class Worker(db.Model):
    __tablename__ = 'daq_worker'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    project_id = db.Column(db.Integer, db.ForeignKey('daq_project.id'))
    project = db.relationship("Project")

    def __repr__(self):
        return str(self.name)        


class Temperature(db.Model):
    __tablename__ = 'daq_temperature'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('daq_project.id'))
    project = db.relationship("Project")

    worker_id = db.Column(db.Integer, db.ForeignKey('daq_worker.id'))
    worker = db.relationship("Worker")

    datetime = db.Column(db.DateTime)
    value = db.Column(db.Text)

    def __repr__(self):
        return str(self.datetime)


class Power(db.Model):
    __tablename__ = 'daq_power'
    id = db.Column(db.Integer, primary_key=True)

    project_id = db.Column(db.Integer, db.ForeignKey('daq_project.id'))
    project = db.relationship("Project")

    worker_id = db.Column(db.Integer, db.ForeignKey('daq_worker.id'))
    worker = db.relationship("Worker")

    datetime = db.Column(db.DateTime)
    value = db.Column(db.Text)

    def __repr__(self):
        return str(self.datetime)

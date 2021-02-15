from app import db

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    name = db.Column(db.String())

    def __repr__(self):
        return '<id {}-{}>'.format(self.id, self.username)
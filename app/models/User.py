from app import db


class User(db.Model):

    __fillable__ = ['name', 'email']

    def __repr__(self) -> str:
        return '<User %r>' % self.name

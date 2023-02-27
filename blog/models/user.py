from .database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String, unique=True)
    is_staff = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"

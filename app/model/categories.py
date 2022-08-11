from app import db

class Categories(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return "<Category {}>".format(self.code)
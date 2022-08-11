from app import db
from app.model.categories import Categories

class Products(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    code = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.BigInteger, db.ForeignKey(Categories.id, ondelete="CASCADE"))

    def __repr__(self):
        return "<Products {}>".format(self.code)
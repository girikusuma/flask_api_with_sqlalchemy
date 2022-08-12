from app import db
from app.model.products import Products

class ProductGalery(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    product_id = db.Column(db.BigInteger, db.ForeignKey(Products.id, ondelete="CASCADE"))
    title = db.Column(db.String(50), nullable=True)
    path = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "<Galery {}>".format(self.path)
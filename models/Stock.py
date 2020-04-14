from app import db
from datetime import datetime

class StockModel(db.Model):
    __tablename__='new_stock'
    id= db.Column(db.Integer, primary_key=True)
    invid=db.Column(db.Integer, db.ForeignKey('new_inventories.id'))
    quantity=db.Column(db.Integer)
    created_at=db.Column(db.DateTime, default=datetime.utcnow)

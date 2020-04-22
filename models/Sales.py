from main import db
from datetime import datetime

class SalesModel(db.Model):
    __tablename__='new_sales'
    id= db.Column(db.Integer, primary_key=True)
    invid=db.Column(db.Integer, db.ForeignKey('new_inventories.id'))
    quantity=db.Column(db.Integer)
    created_at=db.Column(db.DateTime, default=datetime.utcnow)

    def add_sale(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_sales_by_id(cls,invid):
        return cls.query.filter_by(invid=invid).all()
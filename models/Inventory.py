from main import db

class InventoryModel(db.Model):
    __tablename__='new_inventories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    inv_type=db.Column(db.String(10),nullable=False)
    buying_price=db.Column(db.Float)
    selling_price=db.Column(db.Float, nullable=False)

    sales = db.relationship('SalesModel', backref='inventories', lazy=True)
    stock = db.relationship('StockModel', backref='inventories', cascade="all, delete-orphan",lazy=True)

    def add_inventories(self):
        db.session.add(self)
        db.session.commit()

        #classMethod

    @classmethod
    def fetch_all_inventories(cls):
        return cls.query.all()
    

    


    


    
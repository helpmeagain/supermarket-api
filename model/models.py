from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  
class Manufacturer(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  price = db.Column(db.Float, nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
  manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'), nullable=False)
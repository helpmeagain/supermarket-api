from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

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
  
class CategorySchema(ma.Schema):
  class Meta:
    fields = ('id', 'title')
    
class ManufacturerSchema(ma.Schema):
  class Meta:
    fields = ('id', 'title')
    
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'title', 'price', 'category_id', 'manufacturer_id')

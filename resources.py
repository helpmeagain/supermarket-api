from flask_restful import Resource, reqparse
from flask import jsonify
from models import db, Category, Manufacturer, Product, CategorySchema, ManufacturerSchema, ProductSchema

class CategoryResource(Resource):
  def get(self, category_id=None):
    if category_id is None:
      categories = Category.query.all()
      category_schema = CategorySchema(many=True)
      categories = category_schema.dump(categories), 200
      return jsonify(categories)
    
    category = Category.query.get(category_id)
    return CategorySchema().dump(category), 200
  
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True)
    args = parser.parse_args()
    
    category = Category(title=args['title'])
    db.session.add(category)
    db.session.commit()
    
    return CategorySchema().dump(category), 201
  
  def put(self, category_id):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True)
    args = parser.parse_args()
    
    category = Category.query.get(category_id)
    category.title = args['title']
    db.session.commit()
    
    return CategorySchema().dump(category), 200
  
  def delete(self, category_id):
    category = Category.query.get(category_id)
    db.session.delete(category)
    db.session.commit()
    
    return '', 204
  
class ManufacturerResource(Resource):
  def get(self, manufacturer_id=None):
    if manufacturer_id is None:
      manufacturers = Manufacturer.query.all()
      manufacturer_schema = ManufacturerSchema(many=True)
      manufacturers = manufacturer_schema.dump(manufacturers), 200
      return jsonify(manufacturers)
    
    manufacturer = Manufacturer.query.get(manufacturer_id)
    return ManufacturerSchema().dump(manufacturer), 200
  
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True)
    args = parser.parse_args()
    
    manufacturer = Manufacturer(title=args['title'])
    db.session.add(manufacturer)
    db.session.commit()
    
    return ManufacturerSchema().dump(manufacturer), 201
  
  def put(self, manufacturer_id):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True)
    args = parser.parse_args()
    
    manufacturer = Manufacturer.query.get(manufacturer_id)
    manufacturer.title = args['title']
    db.session.commit()
    
    return ManufacturerSchema().dump(manufacturer), 200
  
  def delete(self, manufacturer_id):
    manufacturer = Manufacturer.query.get(manufacturer_id)
    db.session.delete(manufacturer)
    db.session.commit()
    
    return '', 204
  
class ProductResource(Resource):
  def get(self, product_id=None):
    if product_id is None:
      products = Product.query.all()
      product_schema = ProductSchema(many=True)
      products = product_schema.dump(products), 200
      return jsonify(products)
    
    product = Product.query.get(product_id)
    return ProductSchema().dump(product), 200
  
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True)
    parser.add_argument('price', type=float, required=True)
    parser.add_argument('category_id', type=int, required=True)
    parser.add_argument('manufacturer_id', type=int, required=True)
    args = parser.parse_args()
    
    product = Product(title=args['title'], price=args['price'], category_id=args['category_id'], manufacturer_id=args['manufacturer_id'])
    db.session.add(product)
    db.session.commit()
    
    return ProductSchema().dump(product), 201
  
  def put(self, product_id):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True)
    parser.add_argument('price', type=float, required=True)
    parser.add_argument('category_id', type=int, required=True)
    parser.add_argument('manufacturer_id', type=int, required=True)
    args = parser.parse_args()
    
    product = Product.query.get(product_id)
    product.title = args['title']
    product.price = args['price']
    product.category_id = args['category_id']
    product.manufacturer_id = args['manufacturer_id']
    db.session.commit()
    
    return ProductSchema().dump(product), 200
  
  def delete(self, product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    
    return '', 204
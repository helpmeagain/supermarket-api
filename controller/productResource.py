from flask_restful import Resource, reqparse
from flask import jsonify
from model.models import db, Product
from model.schemas import ProductSchema

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
from flask_restful import Resource, reqparse
from flask import jsonify
from model.models import db, Category
from model.schemas import CategorySchema

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
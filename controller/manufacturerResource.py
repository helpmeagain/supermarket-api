from flask_restful import Resource, reqparse
from flask import jsonify
from model.models import db, Manufacturer
from model.schemas import ManufacturerSchema

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
from flask_marshmallow import Marshmallow
ma = Marshmallow()

class CategorySchema(ma.Schema):
  class Meta:
    fields = ('id', 'title')
    
class ManufacturerSchema(ma.Schema):
  class Meta:
    fields = ('id', 'title')
    
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'title', 'price', 'category_id', 'manufacturer_id')
from flask import Flask
from flask_restful import Api
from model.models import db
from model.schemas import ma
from controller.categoryResource import CategoryResource
from controller.manufacturerResource import ManufacturerResource
from controller.productResource import ProductResource
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
api = Api(app)
db.init_app(app)
ma.init_app(app)

api.add_resource(CategoryResource, '/categories', '/categories/<int:category_id>')
api.add_resource(ManufacturerResource, '/manufacturers', '/manufacturers/<int:manufacturer_id>')
api.add_resource(ProductResource, '/products', '/products/<int:product_id>')

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint( SWAGGER_URL, API_URL,
    config={  
        'app_name': "supermarket-api"
    },
)

app.register_blueprint(swaggerui_blueprint)

with app.app_context():
  db.create_all()

if __name__ == '__main__':
  app.run(debug=True)
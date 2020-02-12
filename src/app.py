from flask import Flask, Blueprint, jsonify
from flask_restful import Api
from routes.base import base_blueprint
from routes.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

print('Registering blueprints...')
app.register_blueprint(base_blueprint)

print('Initializing flask-restful routes...')
initialize_routes(api)

@app.errorhandler(404)
def unknown_urls(req):
    return jsonify({ "error": "The resource you are looking for does not exist." }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')
from flask import Response, request, jsonify
from flask_restful import Resource
import json

class PeopleAPI(Resource):
    def get(req):
        return Response(json.dumps({ 'name': 'Bruce Wayne' }), status=200, mimetype='application/json')
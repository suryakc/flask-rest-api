from flask import Blueprint, Response, request, jsonify
from flask_restful import Resource
from constants import BASE_URL

base_blueprint = Blueprint('', __name__, url_prefix=BASE_URL)

@base_blueprint.route("/")
def root():
    return "API is at /api/v1"

@base_blueprint.route("/health")
def health():
    return jsonify({ "status": "up" }), 200


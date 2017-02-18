import os
from flask import Blueprint, current_app, jsonify, make_response
from flask_restful import Api, Resource
import logging

logger = logging.getLogger(__name__)

api_bp = Blueprint('api', __name__)

class MyApi(Api):
    pass

class ShowPort(Resource):
    def get(self):
        logger.info("GET method trigged, will return the current listening port")
        return make_response(jsonify({'RunningOnPort': current_app.config["PORT"]}), 200)

    def put(self):
        logger.info("PUT method trigged, will do nothing")
        return make_response(jsonify({"msg": "Currently no handler for put method, nothing is done"}), 200)

api = MyApi(api_bp, catch_all_404s=True)
api.add_resource(ShowPort, '/')

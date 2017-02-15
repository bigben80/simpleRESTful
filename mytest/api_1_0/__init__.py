import os
from flask import Blueprint, current_app
from flask_restful import Api, Resource
import logging

logger = logging.getLogger(__name__)

api_bp = Blueprint('api', __name__)

class TestApi(Api):
    pass

class ShowPort(Resource):
    def get(self):
        logger.info("GET method trigged, will return the current listening port")
        return {'RunningOnPort': current_app.config["PORT"]}

    def put(self):
        logger.info("PUT method trigged, will do nothing")
        return "Currently no handler for put method, nothing is done"

api = TestApi(api_bp, catch_all_404s=True)
api.add_resource(ShowPort, '/')

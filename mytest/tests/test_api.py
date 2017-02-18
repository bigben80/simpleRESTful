import unittest
from flask import current_app, Flask, Blueprint, request, jsonify
from flask_restful import Api
from mytest import create_app
from mytest.api_1_0 import ShowPort, MyApi
from mytest.config import DebugConfig as debug_config
import json


class BasicTestCase(unittest.TestCase):
    """ Test case without blue print
    """
    def setUp(self):
        self.app = create_app()
        self.app.context = self.app.app_context()
        self.app.context.push()
        self.client = self.app.test_client()
        

    def tearDown(self):
        self.app.context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

from mytest.api_1_0 import MyApi

class BluePrintTestCase(unittest.TestCase):
    """ Test case with blue print
    """

    def test_get_api(self):
        bp = Blueprint('test', __name__)
        api = MyApi(bp)
        app = Flask(__name__)
        app.config.from_object(debug_config)
        app.register_blueprint(bp)
        api.add_resource(ShowPort, '/')

        with app.test_client() as test_client:
            resp = test_client.get('/')
            data = json.loads(resp.data)
            self.assertEquals(data['RunningOnPort'], current_app.config["PORT"])
        

    def test_put_api(self):
        bp = Blueprint('test', __name__)
        api = MyApi(bp)
        app = Flask(__name__)
        app.config.from_object(debug_config)
        app.register_blueprint(bp)
        api.add_resource(ShowPort, '/')

        with app.test_client() as test_client:
            resp = test_client.put('/')
            data = json.loads(resp.data)
            self.assertEquals(data['msg'], "Currently no handler for put method, nothing is done")
        

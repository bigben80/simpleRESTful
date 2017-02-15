import unittest
from flask import current_app, Flask, Blueprint
from flask_restful import Api
from mytest import create_app


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

    def test_api(self):
        pass

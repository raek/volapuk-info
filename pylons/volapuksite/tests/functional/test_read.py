from volapuksite.tests import *

class TestReadController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='read', action='index'))
        # Test response...

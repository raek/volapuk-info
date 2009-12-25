from volapuksite.tests import *

class TestLearnController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='learn', action='index'))
        # Test response...

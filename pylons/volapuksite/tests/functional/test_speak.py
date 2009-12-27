from volapuksite.tests import *

class TestSpeakController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='speak', action='index'))
        # Test response...

from volapuksite.tests import *

class TestDeliciouskAccountController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='delicious_account', action='index'))
        # Test response...

from datetime import datetime

class Blog(object):
    
    def __init__(self):
        self.last_updated = datetime.fromordinal(1)


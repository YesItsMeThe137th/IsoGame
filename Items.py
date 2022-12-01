class Items:
    def __init__(self, location):
        self.location = location
        
class Gold(Items):
    def __init__(self, location):
        super.__init__(location)

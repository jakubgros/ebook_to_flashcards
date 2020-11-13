class Feature:
    def __init__(self, function, description):
        self.function = function
        self.description = description

    def run(self, data):
        self.function(data)
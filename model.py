class Model(): 
    def __init__(self): 
        print("In Parent")

    def transformData(self,value):
        raise NotImplementedError()

    def train(self, data): 
        raise NotImplementedError()
    
    def predict(self, data):
        raise NotImplementedError()

from model import Model

class PositiveModel(Model): 

    def transformData(self,value): 
        return 1

    def train(self,value): 
        return
    
    def predict(self,value): 
        return 1
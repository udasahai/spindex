from model import Model

# Pipeline class is responsible to split the dataset as per the configuration file and run the model on it . 
# It manipulates the data as per the configuration file and runs train and predict on the data. 

class Pipeline(): 
    model : Model = None 
    data = None 

    def __init__(self): 
        print("Initializing the pipleline class")
    
    def setModel(self,model): 
        self.model = model

    def setData(self,data): 
        self.data = data


from postiveModel import parentlessModel,PositiveModel

def main():
    print("Entering the program")
    model =  parentlessModel()
    model.sysout()
    model2 = PositiveModel() 
    print(model2.transformData(1))

    
if __name__ == "__main__": main()
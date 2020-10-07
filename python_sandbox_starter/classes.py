# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class Cars:
    # constructor
    def __init__(self,make,modelYear):
        self.carName=make
        self.carModelYear=modelYear

    def showSpecs(self):
        print(f'Car\'s make is {self.carName} and Car\'s Year is {self.carModelYear}')

class bmw(Cars):
    def __init__(self,make,year,speed):
        self.carName=make
        self.carModelYear=year
        self.speed=speed
    
    def showSpecs(self):
        print(f'Car\'s name is {self.carName} , model year is {self.carModelYear} , speed is {self.speed}')

c1=Cars('Toyota',2016)

c1.showSpecs()

c2= bmw('BMW Sports',2018,280)

c2.showSpecs()
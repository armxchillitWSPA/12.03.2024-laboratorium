class Car:
    def __init__(self,brand,model,year_of_issue):
        self.brand = brand
        self.model = model
        self.year_of_issue = year_of_issue

car1 = Car("Mercedes", "a45", 2016)
car2 = Car("Volkswagen","Passat", 2005)

print(car1.brand)
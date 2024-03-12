class Employee:
    def __init__(self,first_name,last_name,position,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary

employee1 = Employee("Danya","Litvin","Старший слесарщик",4000)
print(employee1.first_name,employee1.last_name,employee1.position,employee1.salary)
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

obiekt1 = Person("Ihor","Kublytskyi",19)
obiekt2 = Person("Artemij","Matvienko",8)
obiekt3 = Person("Ewa","Raczkowska",42)

print(obiekt1.first_name,obiekt1.last_name,obiekt1.age)
print(obiekt2.first_name,obiekt2.last_name,obiekt2.age)
print(obiekt3.first_name,obiekt3.last_name,obiekt3.age)

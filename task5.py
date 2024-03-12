class Pet:
    def __init__(self,name,species):
        self.name  = name 
        self.species = species 

pet1 = Pet("Szarik","Cat")
pet2 = Pet("Danya","Dog")

print(pet1.name,pet1.species)   
print(pet2.name,pet2.species)

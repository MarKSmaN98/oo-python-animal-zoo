#from lib.animal import Animal

class Zoo:
    instances = []
    species = []
    names = []
    animals = []

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.__class__.instances.append(self)

    @classmethod
    def all(cls):
        for i in cls.instances:
            print(i.name + i.location)
        pass

    def animal_species(self):
        for i in self.species:
            return i

    def find_by_species(self, species):
        return_list = []
        for i in self.species:
            if i.species == species:
                return_list.append(i)
        return return_list

    def animal_nicknames(self):
        pass

    @classmethod
    def find_by_location(cls, location):
        return_list = []
        for i in cls.instances:
            if i.location == location:
                return_list.append(i)
        return return_list

    

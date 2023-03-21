from lib.zoo import Zoo
class Animal(Zoo):
    instances = []

    def __init__(self, zoo, nick_name, weight, species):
        self.zoo = zoo
        self.nick_name = nick_name
        self.weight = weight
        self.species = species
        self.__class__.instances.append(self)
        
        super().animals.append(self)
        super().names.append(nick_name)
        if (not nick_name in super().species):
            super().species.append(species)

    @classmethod
    def all(cls):
        for i in cls.instances:
            print(i)

    @classmethod
    def find_by_species(cls, species):
        return_list = []
        for i in cls.instances:
            if i.species == species:
                return_list.append(i)
        return return_list
    

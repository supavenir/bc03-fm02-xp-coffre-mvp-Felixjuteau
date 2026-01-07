from tresore import Tresore
class Chest:

    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        self.size = size
        self.tresore_list= []
        self.total_value = 0
    def get_size(self):
        return self.size

    def get_tresors_list(self):
        return self.tresore_list

    def remove(self,tresore: Tresore):
        self.tresore_list.remove(tresore)
        self.total_value -=tresore.value

    def add(self, tresore: Tresore):
        if not isinstance(tresore, Tresore):
            raise ValueError("fo-tresor detecte")

        total_weight = self.total_weight()
        if self.size < total_weight + tresore.getWeight():
            raise Exception("objects trop lourds à ajouter")
        if tresore in self.tresore_list:
            raise Exception("Duplicated tresore")

        self.tresore_list.append(tresore)
        self.total_value +=tresore.value

    def total_weight(self):
        weight = 0
        for tresor in self.tresore_list:
            weight += tresor.getWeight()
        return weight

    def shearch_tresore(self, name):
        
        for tresor in self.tresore_list :
            if tresor.name == name:
                return tresor
        
        return None
    
    def get_value(self):
        return self.total_value
    

from tresore import Tresore
class Chest:

    def __init__(self, size, lock=False):
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        self.lock = lock
        self.size = size
        self.tresore_list= []

    def get_size(self):
        return self.size

    def get_tresors_list(self):
        return self.tresore_list

    def remove(self,tresore: Tresore):
        if self.lock :
            raise Exception("coffre verouillé impossible de retirer des tresore")
        self.tresore_list.remove(tresore)

    def add(self, tresore: Tresore):
        if self.lock :
            raise Exception("coffre verouillé impossible d'ajouter des tresore")
        if not isinstance(tresore, Tresore):
            raise ValueError("fo-tresor detecte")

        total_weight = self.total_weight()
        if self.size < total_weight + tresore.getWeight():
            raise Exception("objects trop lourds à ajouter")
        if tresore in self.tresore_list:
            raise Exception("Duplicated tresore")
        

        self.tresore_list.append(tresore)

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

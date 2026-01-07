from tresore import Tresore
class Chest:

    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        self.size = size
        self.tresore_list= []

    def get_size(self):
        return self.size
    
    def get_tresors_list(self):
        return self.tresore_list

    def remove(self,tresore: Tresore):
        self.tresore_list.remove(tresore)
    
    def add(self, tresore: Tresore):
        if not isinstance(tresore, Tresore):
            raise ValueError("fo-tresor detecte")
        
        if len(self.tresore_list) >= self.size:
            raise Exception("Chest is full")
        
        if tresore in self.tresore_list:
            raise Exception("Duplicated tresore")

        self.tresore_list.append(tresore)

    def shearch_tresore(self, name):
        
        for tresor in self.tresore_list :
            if tresor.name == name:
                return tresor
        
        return None
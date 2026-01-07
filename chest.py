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
        return self.tresors_list

    def add(self,tresore: Tresore):
        self.tresore_list.append(tresore)

    def remove(self,tresore: Tresore):
        self.tresore_list.remove(tresore)
    
    def add(self, tresore: Tresore):
        if isinstance(tresore, Tresore):
            self.tresore_list.append(tresore)
        else:
            raise ValueError("fo-tresor detecte")
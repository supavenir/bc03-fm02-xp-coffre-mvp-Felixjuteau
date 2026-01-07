from tresore import Tresore
class Chest:

    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        self.size = size
        self.tresore_list= []

    def get_size(self):
        return self.size
    
    def add(self,tresore: Tresore):
        self.tresore_list.append(tresore)
class Chest:

    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        self.size = size

    def get_size(self):
        return self.size
import time 

class Player:
    def __init__(self, name):
        self.name = name 
        self.points = 0

    def __str__(self):
        return f"It's {self.name}'s turn.\n"

    def update_points(self):
        self.points += 1

    def delay(self):
        time.sleep(0.5)
    




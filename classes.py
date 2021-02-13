class Point():
    #automatically called everytime we create a new Point
    #stored inside object itself: self
    #point in x and y coordinate system
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

flight = Flight(3)
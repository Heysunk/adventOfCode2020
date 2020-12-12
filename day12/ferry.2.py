# create data structure with neighbours (the adapters that can be reached from this one)
# solve recursively bottom up, so we always pass the highest value from the previous one, and multiply it by the amount of neighbours

#assume already sorted

dirArray = ['E', 'S', 'W', 'N']
class Ferry:
    def __init__(self):
        self.facingDir = 0
        self.coords = [0,0]
        self.waypoint = [1,10]
    def move(self, direction, value):
        if direction == "N":
            self.waypoint[0] += value
            return
        elif direction == "S":
            self.waypoint[0] -= value
            return
        elif direction == "E":
            self.waypoint[1] += value
            return
        elif direction == "W":
            self.waypoint[1] -= value
            return
        elif direction == "F":
            for i in range(0, value):
                self.coords[0] += self.waypoint[0]
                self.coords[1] += self.waypoint[1]
            return
        elif direction == "R" or direction == "L":
            rotation = 1
            if direction == "L":
                rotation = -1

            newDir = value/90
            newDir = int(newDir%4)
            for i in range(0, newDir):
                y0 = self.waypoint[0]
                x0 = self.waypoint[1]
                self.waypoint[0] = (-x0 * rotation)
                self.waypoint[1] = (y0 * rotation)
            return
        else:
            raise ValueError("Invalid direction: " + direction)

    def calcManhattanDistance(self, origin):
        return abs(origin[0] + self.coords[0]) + abs(origin[1] + self.coords[1])


directions = []
with open("input.txt") as file_in:
    for line in file_in:
        line = (line.rstrip())
        direction = line[0]
        value = line[1:]
        directions.append( (direction, int(value)) )
ferry = Ferry()
for item in directions:
    direction, value = item
    ferry.move(direction, value)

print(ferry.calcManhattanDistance([0,0]))

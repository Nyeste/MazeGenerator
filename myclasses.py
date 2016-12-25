class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Cell:
    def __init__(self):
        self.visited = False
        self.walls = []

    def addWall(self, wall):
        self.walls.append(wall)

    def addWalls(self):
        self.addWall(Wall(Direction.NORTH))
        self.addWall(Wall(Direction.EAST))
        self.addWall(Wall(Direction.SOUTH))
        self.addWall(Wall(Direction.WEST))
        
class Wall:
    def __init__(self, dir):
        self.passable = False
        self.direction = dir

    def setPassable(self, state):
        self.passable = state

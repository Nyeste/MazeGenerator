import random

class Position:
    def __init__(self,i,j):
        self.row = i
        self.col = j


class Cell:

    def __init__(self,i,j):
        self.visited = False
        self.id = Position(i,j)
        self.walls = []

    def add_wall_between(self, other):
        wall = Wall(self.id,other.id)
        self.add_wall(wall)
        other.add_wall(wall)
        return wall

    def add_wall(self,mywall):
        self.walls.append(mywall)

    def visit(self):
        self.visited = True

    def select (self):
        self.visited = True
        return self.walls

    def only_one_is_visited(self, other):
        if(self.visited and not other.visited) or (not self.visited and other.visited):
            return True
        else:
            return False

class Wall:
    no_walls = 0

    def __init__(self, cellid1, cellid2):
        self.passable = False
        self.cell_id_1 = cellid1
        self.cell_id_2 = cellid2
        self.id = Wall.no_walls
        Wall.no_walls += 1

    def setPassable(self, state):
        self.passable = state

class Grid:
    def __init__(self,no_rows,no_cols):
        self.cells = [[0 for j in range(no_rows)] for i in range(no_cols)]
        self.walls = []
        self.working_walls = []
        self.no_rows = no_rows
        self.no_cols = no_cols
        for i in range (0, no_rows):
            for j in range(0, no_cols):
                self.cells[i][j] = Cell(i,j)

        self.setup_walls()

    def setup_walls(self):
        for i in range (0, self.no_rows-1):
            for j in range(0, self.no_cols-1):
                if i < self.no_rows:
                    self.walls.append(Cell.add_wall_between (self.cells[i][j], self.cells[i+1][j]))
                if j < self.no_cols:
                    self.walls.append(Cell.add_wall_between (self.cells[i][j], self.cells[i][j+1]))

    def the_works(self,start_row, start_col):
        self.working_walls.extend(self.cells[start_row][start_col].select())
        self.process_working_walls()
        while (self.get_non_visited_cell() != False):
            self.working_walls.extend(self.get_non_visited_cell())
            self.process_working_walls()


    def get_non_visited_cell(self):
        for i in range (0, self.no_rows-1):
            for j in range(0, self.no_cols-1):
                if not self.cells[i][j].visited:
                    return self.cells[i][j]
        return False

    def process_working_walls(self):
        while (self.working_walls.count>0):
            self.process_working_wall(random.randint(0,len(self.working_walls)-1))

    def process_working_wall(self,index):
        if Cell.only_one_is_visited(self.get_cell(self.working_walls[index].cell_id_1),self.get_cell(self.working_walls[index].cell_id_2)):
            self.working_walls[index].setPassable(True)
            for w in self.walls:
                if w.id == self.working_walls.id:
                    w.setPassable(True)
            self.add_to_working_walls(self.get_cell(self.working_walls[index].cell_id_1),self.get_cell(self.working_walls[index].cell_id_2))
        self.working_walls.remove(index)

    def get_cell(self, pos):
        return self.cells[pos.row][pos.col]

    def add_to_working_walls(self, cell1,cell2):
        if(not cell1.visited):
            self.working_walls_extend(cell1.select())
        if(not cell2.visited):
            self.working_walls_extend(cell2.select())

#!/usr/bin/python
import random

class EnergyGrid:
    
    grid = None # 2D Array of Ints
    width = 0
    height = 0
    
    def __init__(self):
        random.seed()
        self.width = 35
        self.height = 35
        self.create_grid(self.width, self.height)
        self.populate_grid()

    def create_grid(self, x, y):
        '''Create the grid and zero the fields'''
        self.grid = []
        for i in range(0, x):
            temp_grid = []
            for i in range(0, y):
                temp_grid.append(0x0)
            self.grid.append(temp_grid)

    def spawn_poh(self, fract):
        # Spawn POH randomly in upper area of grid (0x1)
        randx = random.randrange(0, self.width/fract)
        randy = random.randrange(0, self.height/fract)
        self.grid[randx][randy] = 0x1

    def spawn_cores(self, fract, cores):
        # Spawn seven energy cores in random locations 
        # not in the same location as the spawn area.
        resx = range(0, self.width/fract)
        resy = range(0, self.height/fract)
        for i in range(0, cores):
            while True:
                passed = True
                randx = random.randrange(0, self.width)
                randy = random.randrange(0, self.height)
                if randx in resx and randy in resy: 
                    passed = False
                if self.grid[randx][randy]: 
                    passed = False
                trans_coord = [(-1, -1), (-1, 0), (1, -1),
                               (-1, 0), (1, 0),
                               (-1, 1), (0, 1), (1, 1)]
                for i in trans_coord:
                    bx = randx + i[0]
                    by = randy + i[1]
                    if bx < self.width and by < self.height:
                        if self.grid[bx][by] != 0x0:
                            passed = False
                    else: passed = False
                if passed: break
            self.grid[randx][randy] = 0x2

    def populate_grid(self):
        self.spawn_poh(5)
        self.spawn_cores(5, 7)

    def print_grid(self):
        for i in self.grid:
            print "".join(str(j) + " " for j in i)
        

def main():
    energy_grid = EnergyGrid()
    energy_grid.print_grid()
if __name__ == "__main__":
    main()

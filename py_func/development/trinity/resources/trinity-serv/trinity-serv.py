#!/usr/bin/python
import random

class EnergyGrid:
    
    grid = None # 2D Array of Ints
    width = 0
    height = 0
    launch_c = None
    cores_c = []
    towers_c = []
    guards_c = []
    guards_p = {}
    
    def __init__(self):
        random.seed()
        self.width = 35
        self.height = 35
        self.create_grid(self.width, self.height)
        self.populate_grid(5, 15)

    def create_grid(self, x, y):
        '''Create the grid and zero the fields'''
        self.grid = []
        for i in range(0, x):
            temp_grid = []
            for i in range(0, y):
                temp_grid.append(0x0)
            self.grid.append(temp_grid)

    def spawn_poh(self, fract):
        '''Spawn POH randomly in upper area of grid.'''
        randx = random.randrange(0, self.width/fract)
        randy = random.randrange(0, self.height/fract)
        self.grid[randx][randy] = 0x1
        self.launch_c = (randx, randy)

    def spawn_cores(self, fract, cores):
        '''Spawn energy cores in random locations 
        not in the same location as the spawn
        area and other core areas.'''
        resx = range(0, self.width/fract)
        resy = range(0, self.height/fract)
        for i in range(0, cores):
            while True:
                passed = True
                randx = random.randrange(0, self.width)
                randy = random.randrange(0, self.height)
                if randx in resx and randy in resy: 
                    passed = False
                if self.grid[randx][randy] != 0x0: 
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
            self.cores_c.append((randx, randy))

    def spawn_towers(self):
        '''Spawn towers adjacent to energy cores.'''
        trans_coord = [(-2, -2), (-2, 0), (2, -2),
                       (-2, 0), (2, 0),
                       (-2, 2), (0, 2), (2, 2)]
        for i in self.cores_c:
            while True:
                randx, randy = trans_coord[random.randrange(0, 8)]
                randx = randx + i[0]
                randy = randy + i[1]
                if randx >= self.width or randy >= self.height: continue
                if self.grid[randx][randy] != 0x0: continue
                self.grid[randx][randy] = 0x3
                self.towers_c.append((randx, randy))
                break

    def spawn_guards(self, fract, guards):
        '''Spawn guards in empty random locations.'''
        resx = range(0, self.width/fract)
        resy = range(0, self.height/fract)
        for i in range(0, guards):
            while True:
                passed = True
                randx = random.randrange(0, self.width)
                randy = random.randrange(0, self.height)
                if randx in resx and randy in resy: 
                    passed = False
                if self.grid[randx][randy] != 0x0: 
                    passed = False
                if passed: break
            self.grid[randx][randy] = 0x4
            self.guards_c.append((randx, randy))

    def spawn_terrain(self):
        # Not implemented yet.
        pass

    def find_guard_paths(self, distance):
        for i in self.guards_c:
            temp_path = [i]
            for j in range(0, distance):
                while True:
                    trans_coord = [(-1, -1), (-1, 0), (1, -1),
                                   (-1, 0), (1, 0),
                                   (-1, 1), (0, 1), (1, 1)]
                    offx, offy = trans_coord[random.randrange(0, 8)]
                    li = temp_path[-1:][0]
                    pr_c = (li[0] + offx, li[1] + offy)
                    if pr_c[0] >= self.width or pr_c[1] >= self.height:
                        continue
                    if self.grid[pr_c[0]][pr_c[1]] != 0x0:
                        continue
                    if pr_c in temp_path:
                        continue
                    temp_path.append(pr_c)
                    break
            temp_path = temp_path[:-1] + temp_path[::-1]
            self.guards_p[i] = temp_path[:-1]
#            print "%8s: %s" % (i, temp_path)
            

    def populate_grid(self, fract, density):
        if fract != 1:
            # Spawn entities
            self.spawn_poh(fract)
            self.spawn_cores(fract, density)
            self.spawn_towers()
            self.spawn_guards(fract, density)
            self.spawn_terrain()

            # Path find for guards
            self.find_guard_paths(5)
        else:
            print "Fract value cannot be 1."
            exit()

    def print_grid(self):
        for i in self.grid:
            print "".join(str(j) + " " for j in i)
#        print "Launch: (%d, %d)" % self.launch_c
#        print "Cores: %s" % "".join( "(%d, %d), " % (i,v) 
#                                     for i, v in self.cores_c)[0:-2]

class EnergyGridEngine:

    grid = None

    def __init__(self, energy_grid):
        self.grid = energy_grid

    def start(self):
        pass

    def get_log(self):
        pass

def main():
    energy_grid = EnergyGrid()
    energy_grid.print_grid()
#    print energy_grid.guards_p
    energy_grid_engine = EnergyGridEngine(energy_grid)

if __name__ == "__main__":
    main()

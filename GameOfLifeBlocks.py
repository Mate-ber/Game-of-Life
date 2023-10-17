import turtle
import random

STARTING_POSITIONS = [-20, 0, 20]
check_pos = [(-20, -20), (0, 20), (0, -20), (20, 0), (20, -20)]


# 5 x 5
class Cell:
    def __init__(self):
        self.grid = []
        self.grid_turtle = []
        self.grid_k = []
        self.remove_turtle = []
        self.grid_r = []
        self.start_cnt = 5
        self.creating_grid()

    def creating_grid(self):
        cnt = self.start_cnt
        ioi = 0
        while cnt > 0:
            square = turtle.Turtle()
            square.shape("square")
            square.color("black")
            square.penup()
            # cor_x = random.choice(STARTING_POSITIONS)
            # cor_y = random.choice(STARTING_POSITIONS)
            # cor = (cor_x, cor_y)
            cor = check_pos[ioi]
            ioi += 1
            is_nin = True
            for i in range(len(self.grid)):
                if cor in self.grid:
                    is_nin = False
                    break
            if is_nin:
                self.grid.append(cor)
                square.goto(cor)
                self.grid_turtle.append(square)
                cnt -= 1
            else:
                square.hideturtle()

    def check_kill(self):
        for i in range(len(self.grid)):
            neighbors_cnt = 0
            xy = self.grid[i]
            x = xy[0]
            y = xy[1]
            neighbors = [(x-20, y+20), (x-20, y), (x-20, y-20), (x, y+20), (x, y-20), (x+20, y+20), (x+20, y), (x+20, y-20)]
            for j in range(len(neighbors)):
                if neighbors[j] in self.grid:
                    neighbors_cnt += 1
            if neighbors_cnt == 2 or neighbors_cnt == 3:
                self.grid_k.append(xy)
            else:
                self.remove_turtle.append(i)

    def check_resurrect(self):
        min_x = 10000
        min_y = 10000
        max_x = -10000
        max_y = -10000
        for i in range(len(self.grid)):
            min_x = min(min_x, self.grid[i][0])
            min_y = min(min_y, self.grid[i][1])
            max_x = max(max_x, self.grid[i][0])
            max_y = max(max_y, self.grid[i][1])

        for x in range(min_x-20, max_x+40, 20):
            for y in range(min_y-20, max_y+40, 20):
                go = True
                cor = (x, y)
                if cor in self.grid:
                    go = False
                if go:
                    neighbors_cnt = 0
                    neighbors = [(x - 20, y + 20), (x - 20, y), (x - 20, y - 20), (x, y + 20), (x, y - 20), (x + 20, y + 20), (x + 20, y), (x + 20, y - 20)]
                    for z in range(len(neighbors)):
                        if neighbors[z] in self.grid:
                            neighbors_cnt += 1
                    if neighbors_cnt == 3:
                        self.grid_r.append(cor)

    def update_grid(self):
    #    print(f"saw:{self.grid}")
        arr_cleaner = []
        self.grid_k = []
        self.remove_turtle = []
        self.grid_r = []
        print(self.grid_k, self.grid_r, self.remove_turtle)

        self.check_kill()
        self.check_resurrect()

        new_grid_turtle = []
        checker = self.grid
        self.grid = self.grid_k

        for i in range(len(checker)):
            if checker[i] not in self.grid:
                self.grid_turtle[i].hideturtle()
            else:
                new_grid_turtle.append(self.grid_turtle[i])

        gg = []

        for i in range(len(self.grid_r)):
            if self.grid_r[i] not in checker and self.grid_r[i] not in self.grid:
                gg.append(self.grid_r[i])
                self.grid.append(self.grid_r[i])
        min_x = 1000
        yy = 0
        if len(self.grid) > len(checker):
            print(f"k::{self.grid_k}")
            print(f"r::{self.grid_r}")

        print(self.grid)

        for i in range(len(gg)):
            new_square = turtle.Turtle()
            new_square.shape("square")
            new_square.color("black")
            new_square.penup()
            new_square.goto(gg[i][0], gg[i][1])
            new_grid_turtle.append(new_square)

        self.grid_turtle = new_grid_turtle




import turtle
import random

STARTING_POSITIONS = [(-20, -20), (0, 20), (0, -20), (20, 0), (20, -20)]


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
        for it in range(0, self.start_cnt):

            square = self.creating_tail()
            square.goto(STARTING_POSITIONS[it])
            self.grid.append(STARTING_POSITIONS[it])
            self.grid_turtle.append(square)

    def check_kill(self):
        for i in range(len(self.grid)):

            neighbors_cnt = 0
            neighbors = self.get_neighbours(self.grid[i][0], self.grid[i][1])

            for j in range(len(neighbors)):
                if neighbors[j] in self.grid:
                    neighbors_cnt += 1

            if neighbors_cnt == 2 or neighbors_cnt == 3:
                self.grid_k.append((self.grid[i][0], self.grid[i][1]))
            else:
                self.remove_turtle.append(i)

    def check_resurrect(self):
        minmax = self.get_min_max()
        for x in range(minmax[0]-20, minmax[2]+40, 20):
            for y in range(minmax[1]-20, minmax[3]+40, 20):

                cor = (x, y)
                if cor not in self.grid:

                    neighbors_cnt = 0
                    neighbors = self.get_neighbours(x, y)

                    for z in range(len(neighbors)):
                        if neighbors[z] in self.grid:
                            neighbors_cnt += 1

                    if neighbors_cnt == 3:
                        self.grid_r.append(cor)

    def update_grid(self):
        self.grid_k = []
        self.remove_turtle = []
        self.grid_r = []

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

        for i in range(len(self.grid_r)):

            if self.grid_r[i] not in checker and self.grid_r[i] not in self.grid:
                self.grid.append(self.grid_r[i])

        for i in range(len(self.grid_r)):

            new_square = self.creating_tail()
            new_square.goto(self.grid_r[i][0], self.grid_r[i][1])
            new_grid_turtle.append(new_square)

        self.grid_turtle = new_grid_turtle

    def get_neighbours(self, x, y):
        neighbors = [(x - 20, y + 20), (x - 20, y), (x - 20, y - 20), (x, y + 20), (x, y - 20), (x + 20, y + 20), (x + 20, y), (x + 20, y - 20)]
        return neighbors

    def get_min_max(self):
        min_x = 10000
        min_y = 10000
        max_x = -10000
        max_y = -10000
        for i in range(len(self.grid)):
            min_x = min(min_x, self.grid[i][0])
            min_y = min(min_y, self.grid[i][1])
            max_x = max(max_x, self.grid[i][0])
            max_y = max(max_y, self.grid[i][1])
        return min_x, min_y, max_x, max_y

    def creating_tail(self):
        new_square = turtle.Turtle()
        new_square.shape("square")
        new_square.color("black")
        new_square.penup()
        return new_square

class Черепашка:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise Exception("s меньше либо равно нулю")
        else:
            self.s -= 1
    
    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        return (dx + dy) // self.s + ((dx + dy) % self.s != 0)  # Округляем вверх
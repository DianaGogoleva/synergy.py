class Касса:
    def __init__(self, начальное_количество):
        self.количество = начальное_количество

    def top_up(self, X):
        self.количество += X

    def count_1000(self):
        return self.количество // 1000

    def take_away(self, X):
        if self.количество < X:
            raise Exception("Недостаточно денег в кассе")
        else:
            self.количество -= X
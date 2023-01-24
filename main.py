class TikTacToe:
    def __init__(self):
        self.cell = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def place_crosses(self, x, y):
        if self.cell[x-1][y-1] == "*":
            self.cell[x-1][y-1] == " "
            return 0
        else:
            return 1

    def place_noughts(self, x, y):
        if self.cell[x-1][y-1] == " ":
            self.cell[x-1][y-1] == "0"
            return 0
        else:
            return 1


    def get_winner(self):
        if self.cell[0][0] == self.cell[1][1] == self.cell[0][2] != ' ':
            # победа по диагонали
            symbol = self.cell[0][0]
        elif self.cell[0][2] == self.cell[1][1] == self.cell[2][0] != ' ':
            # победа по диагонали
            symbol = self.cell[0][2]
        elif self.cell[0][0] == self.cell[0][1] == self.cell[0][2] != ' ':
            # победа по первой строке
            symbol = self.cell[0][0]
        elif self.cell[1][0] == self.cell[1][1] == self.cell[1][2] != ' ':
            # победа по второй строке
            symbol = self.cell[1][0]
        elif self.cell[2][0] == self.cell[2][1] == self.cell[2][2] != ' ':
            # победа по третьей строке
            symbol = self.cell[2][0]
        elif self.cell[0][0] == self.cell[1][0] == self.cell[2][0] != ' ':
            # победа по первому столбцу
            symbol = self.cell[0][0]
        elif self.cell[0][1] == self.cell[1][1] == self.cell[2][1] != ' ':
            # победа по второму столбцу
            symbol = self.cell[0][1]
        elif self.cell[0][2] == self.cell[1][2] == self.cell[2][2] != ' ':
            # победа по третьему столбцу
            symbol = self.cell[0][2]


def test_1():
    game = TikTacToe()
    assert game.place_crosses(1, 3) == 1
    assert game.place_crosses(1, 3) == 0
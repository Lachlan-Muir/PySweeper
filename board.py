# representation of minesweeper board

"""
Using two copies of the board, we can maintain one original version (invisible to the player) and one working copy
(showing the tiles revealed to the player).

The player has two available game actions:
1.  Flag
2.  Poke

Flag: marks a point as a mine
Poke: tests a point by revealing it. If the point had a mine, the player loses. If the point was empty, then that
point and all connected empty points are revealed.
"""

class Board:
    def __init__(self, h_board):
        self.width = len(h_board[0])
        self.height = len(h_board)
        self.h_board = h_board
        self.v_board = [['.' for i in range(self.width)] for j in range(self.height)]

    def __str__(self):
        """
         x 0 1 2 3 4 ...
        y
        0  . . . . .
        1  . . . . .
        2  . . . . .
        3  . . . . .
        4  . . . . .
        ...
        """
        output = " x "
        for x in range(self.width):
            output += str(x) + " "
        output += "\n"
        output += "y \n"
        for y in range(self.height):
            output += str(y) + "  " + ' '.join(self.v_board[y]) + "\n"

        return output

    def poke(self, x, y):
        return

    def flag(self, x, y):
        return

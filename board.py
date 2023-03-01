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
    """
    A class representation of a Minesweeper board. Mines are represented by 'M', and empty spaces are represented by
    '.'. Tiles not yet revealed to the player are represented by 'H' and adjacent mine counts are represented by
    integers. Flags places by the player are represented by 'F'.

    Attributes:
        width       The width (x-axis) of the board
        height      The height (y-axis) of the board

    Methods:
        poke(x, y)  Reveals the tile at the given coordinates to the player
        flag(x, y)  Places a flag at the given coordinates
        within_bounds(x, y) Checks if the given x, y coordinates are within the bounds of the board.
    """

    def __init__(self, h_board):
        """
        :param h_board: A two-dimensional array of characters representing the board hidden from the player.
        """
        self.__MINE_TILE = 'M'
        # empty tile only used in hidden board; empty tiles on v_board are represented by their adjacent mine counts
        self.__EMPTY_TILE = '.'
        self.__HIDDEN_TILE = 'H'
        self.__FLAG_TILE = 'F'
        self.width = len(h_board[0])
        self.height = len(h_board)
        # The board hidden from the player
        self.__h_board = h_board
        # The board visible to the player
        self.__v_board = [[self.__HIDDEN_TILE for i in range(self.width)] for j in range(self.height)]


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
            output += str(y) + "  " + ' '.join(self.__v_board[y]) + "\n"

        return output

    def within_bounds(self, x, y):
        """
        Checks if the given coordinates are within the bounds of the board.
        :param x: the x-axis coordinate.
        :param y: the y-axis coordinate.
        :return: True if the coordinates are in bounds, False if they are out.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def poke(self, x, y):
        """
        Takes x and y coordinates and reveals the tile at that location on the board to the player. Nearby tiles
        which do not have mines adjacent to them are also revealed. The hidden board is not modified.

        :param x: the x-axis coordinate. Must be greater than 0 and less than the width of the board.
        :param y: the y-axis coordinate. Must be greater than 0 and less than the height of the board.
        :return: True if a mine was poked, False otherwise
        """
        # make sure we have valid coordinates
        assert self.within_bounds(x, y)

        # check if the tile has been poked before; if it has we don't have to do anything
        if self.__v_board[y][x] == self.__HIDDEN_TILE:
            poked_char = self.__h_board[y][x]

            if poked_char == self.__MINE_TILE:
                # if the tile we poked was a mine, we don't have to do anything other than show it on the visible board,
                # since the game will end as a result.
                self.__v_board[y][x] = poked_char
                return True
            elif poked_char == self.__EMPTY_TILE:
                mine_ct = self.__adjacent_mine_count(x, y)
                self.__v_board[y][x] = str(mine_ct)
                # if the tile was empty and has no adjacent mines, then we want to poke the tiles around it as well
                # so that the player does not have to enter a bunch of unnecessary poke commands
                if mine_ct == 0:
                    for coord in self.__adjacent_coords(x, y):
                        self.poke(coord[0], coord[1])

        return False

    def __adjacent_coords(self, x, y):
        """
        Obtains all coordinates adjacent to the given one. If an adjacent coordinate would be outside the bounds of the
        board, it is not included in the result.
        :param x: the x-axis coordinate. Must be greater than 0 and less than the width of the board.
        :param y: the y-axis coordinate. Must be greater than 0 and less than the height of the board.
        :return: a list of tuples (x, y), each representing a coordinate pair adjacent to the given coordinates.
        """
        # make sure we have valid coordinates
        assert self.within_bounds(x, y)
        #               NW,       N,       NE,      E,      SE,     S,      SW,      W
        translations = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        adj_coords = []
        for t in translations:
            if self.within_bounds(x + t[0], y + t[1]):
                adj_coords.append((x + t[0], y + t[1]))

        return adj_coords

    def __adjacent_tiles(self, x, y):
        """
        Obtains all tiles adjacent to the given one. If an adjacent tile would be outside the bounds of the board, it is
         not included in the result.
        :param x: the x-axis coordinate. Must be greater than 0 and less than the width of the board.
        :param y: the y-axis coordinate. Must be greater than 0 and less than the height of the board.
        :return: a list of characters, each representing a tile adjacent to the given coordinates.
        """
        # make sure we have valid coordinates
        assert self.within_bounds(x, y)
        return list(map(lambda coords : self.__h_board[coords[1]][coords[0]], self.__adjacent_coords(x, y)))

    def __adjacent_mine_count(self, x, y):
        """
        Counts the number of mines adjacent to the given coordinates
        :param x: the x-axis coordinate. Must be greater than 0 and less than the width of the board.
        :param y: the y-axis coordinate. Must be greater than 0 and less than the height of the board.
        :return: an integer count of adjacent mines
        """
        # make sure we have valid coordinates
        assert self.within_bounds(x, y)
        return self.__adjacent_tiles(x, y).count(self.__MINE_TILE)

    def flag(self, x, y):
        """
        Takes x and y coordinates and places a flag at that location on the board visible to the player. The hidden
        board is not modified. If a tile containing a flag is flagged, it will be reverted to a hidden tile.
        :param x: the x-axis coordinate
        :param y: the y-axis coordinate
        :return: None
        """
        # make sure we have valid coordinates
        assert self.within_bounds(x, y)
        return

import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board_3x3 = Board([['b', '.', '.'],
                                ['.', '.', '.'],
                                ['.', '.', '.']])

    def test_init(self):
        self.assertEqual(self.board_3x3.width, 3)
        self.assertEqual(self.board_3x3.height, 3)
        self.assertEqual(self.board_3x3.v_board, [['.', '.', '.'],
                                             ['.', '.', '.'],
                                             ['.', '.', '.']])

    def test_str(self):
        self.assertEqual(" x 0 1 2 \n" +
                         "y \n"       +
                         "0  . . .\n" +
                         "1  . . .\n" +
                         "2  . . .\n", str(self.board_3x3))


if __name__ == '__main__':
    unittest.main()

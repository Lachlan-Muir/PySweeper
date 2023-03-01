import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board_3x3 = Board([['M', '.', '.'],
                                ['.', '.', '.'],
                                ['.', '.', '.']])

    def test_init(self):
        self.assertEqual(self.board_3x3.width, 3)
        self.assertEqual(self.board_3x3.height, 3)
        self.assertEqual(self.board_3x3._Board__v_board, [['H', 'H', 'H'],
                                                          ['H', 'H', 'H'],
                                                          ['H', 'H', 'H']])

    def test_str(self):
        self.assertEqual(" x 0 1 2 \n" +
                         "y \n"       +
                         "0  H H H\n" +
                         "1  H H H\n" +
                         "2  H H H\n", str(self.board_3x3))

    def test_within_bounds(self):
        # test outer edges of board within range
        self.assertTrue(self.board_3x3.within_bounds(0, 0))
        self.assertTrue(self.board_3x3.within_bounds(2, 0))
        self.assertTrue(self.board_3x3.within_bounds(0, 2))
        # test outer edges of board outside range
        self.assertFalse(self.board_3x3.within_bounds(-1, 0))
        self.assertFalse(self.board_3x3.within_bounds(0, -1))
        self.assertFalse(self.board_3x3.within_bounds(3, 0))
        self.assertFalse(self.board_3x3.within_bounds(0, 3))

    def test_adjacent_coords(self):
        # corners
        self.assertEqual([(1, 0), (1, 1), (0, 1)], self.board_3x3._Board__adjacent_coords(0, 0))
        self.assertEqual([(2, 1), (1, 1), (1, 0)], self.board_3x3._Board__adjacent_coords(2, 0))
        self.assertEqual([(1, 1), (2, 1), (1, 2)], self.board_3x3._Board__adjacent_coords(2, 2))
        self.assertEqual([(0, 1), (1, 1), (1, 2)], self.board_3x3._Board__adjacent_coords(0, 2))
        # middle
        self.assertEqual([(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 1)],
                         self.board_3x3._Board__adjacent_coords(1, 1))
        # edges
        self.assertEqual([(2, 0), (2, 1), (1, 1), (0, 1), (0, 0)], self.board_3x3._Board__adjacent_coords(1, 0))
        self.assertEqual([(1, 0), (2, 0), (2, 2), (1, 2), (1, 1)], self.board_3x3._Board__adjacent_coords(2, 1))
        self.assertEqual([(0, 1), (1, 1), (2, 1), (2, 2), (0, 2)], self.board_3x3._Board__adjacent_coords(1, 2))
        self.assertEqual([(0, 0), (1, 0), (1, 1), (1, 2), (0, 2)], self.board_3x3._Board__adjacent_coords(0, 1))

    def test_adjacent_tiles(self):
        self.assertEqual(['.', '.', '.', '.', 'M'], self.board_3x3._Board__adjacent_tiles(1, 0))
        self.assertEqual(['M', '.', '.', '.', '.', '.', '.', '.'], self.board_3x3._Board__adjacent_tiles(1, 1))


    def test_adjacent_mine_count(self):
        self.assertEqual(1, self.board_3x3._Board__adjacent_mine_count(1, 1))
        self.assertEqual(1, self.board_3x3._Board__adjacent_mine_count(1, 0))
        self.assertEqual(0, self.board_3x3._Board__adjacent_mine_count(2, 2))

    def test_poke(self):
        self.assertFalse(self.board_3x3.poke(1, 1))
        self.assertEqual([['H', 'H', 'H'],
                          ['H', '1', 'H'],
                          ['H', 'H', 'H']], self.board_3x3._Board__v_board)
        self.assertFalse(self.board_3x3.poke(2, 2))
        self.assertEqual([['H', '1', '0'],
                          ['1', '1', '0'],
                          ['0', '0', '0']], self.board_3x3._Board__v_board)
        self.assertTrue(self.board_3x3.poke(0, 0))


if __name__ == '__main__':
    unittest.main()

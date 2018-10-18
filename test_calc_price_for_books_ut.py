import unittest

from kata_potter.calc_price_for_books import calc_price_for_books


# Test for function calc_price_for_books
class TestCalcPriceForBooks(unittest.TestCase):

    discount = [0, 1, 0.95, 0.9, 0.80, 0.75]

    def test_no_discounts_available(self):
        self.assertEqual(calc_price_for_books(list([]), self.discount), 0)
        self.assertEqual(calc_price_for_books(list([0]), self.discount), 8)
        self.assertEqual(calc_price_for_books(list([1]), self.discount), 8)
        self.assertEqual(calc_price_for_books(list([2]), self.discount), 8)
        self.assertEqual(calc_price_for_books(list([3]), self.discount), 8)
        self.assertEqual(calc_price_for_books(list([4]), self.discount), 8)
        self.assertEqual(calc_price_for_books(list([0, 0]), self.discount), 8 * 2)
        self.assertEqual(calc_price_for_books(list([1, 1, 1]), self.discount), 8 * 3)

    def test_basic_discounts(self):
        self.assertEqual(calc_price_for_books(list([0, 1]), self.discount), 8 * 2 * 0.95)
        self.assertEqual(calc_price_for_books(list([0, 2, 4]), self.discount), 8 * 3 * 0.9)
        self.assertEqual(calc_price_for_books(list([0, 1, 2, 4]), self.discount), 8 * 4 * 0.8)
        self.assertEqual(calc_price_for_books(list([0, 1, 2, 3, 4]), self.discount), 8 * 5 * 0.75)

    def test_join_discounts(self):
        self.assertEqual(calc_price_for_books(list([0, 0, 1]), self.discount), 8 + (8 * 2 * 0.95))
        self.assertEqual(calc_price_for_books(list([0, 0, 1, 1]), self.discount), 2 * (8 * 2 * 0.95))
        self.assertEqual(calc_price_for_books(list([0, 0, 1, 2, 2, 3]), self.discount), (8 * 4 * 0.8) + (8 * 2 * 0.95))
        self.assertEqual(calc_price_for_books(list([0, 1, 1, 2, 3, 4]), self.discount), 8 + (8 * 5 * 0.75))

    def test_edge_cases(self):
        self.assertEqual(calc_price_for_books(list([0, 0, 1, 1, 2, 2, 3, 4]), self.discount), 2 * (8 * 4 * 0.8))
        self.assertEqual(calc_price_for_books(list([0, 0, 0, 0, 0,
                                                    1, 1, 1, 1, 1,
                                                    2, 2, 2, 2,
                                                    3, 3, 3, 3, 3,
                                                    4, 4, 4, 4]), self.discount),
                         3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8))


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
import unittest

from items import Conjured


class ConjuredTest(unittest.TestCase):
    def test_conjured_quality_decrease_by_two(self):
        item = Conjured("Conjured", 8, 49)
        item.update_at_end_of_day()
        self.assertEquals(7, item.sell_in)
        self.assertEquals(47, item.quality)

    def test_conjured_quality_decrease_by_four_when_expired(self):
        item = Conjured("Conjured", 0, 49)
        item.update_at_end_of_day()
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(45, item.quality)


if __name__ == '__main__':
    unittest.main()

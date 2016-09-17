# -*- coding: utf-8 -*-
import unittest

from items import Item


class ItemTest(unittest.TestCase):
    def test_item_initialization_negative_quality(self):
        with self.assertRaises(AssertionError):
            Item("regular item", 3, -10)

    def test_item_initialization_quality_higher_than_maximum(self):
        with self.assertRaises(AssertionError):
            Item("regular item", 3, 60)

    def test_regular_decrease_by_one(self):
        item = Item("regular item", 3, 10)
        item.update_at_end_of_day()
        self.assertEquals("regular item", item.name)
        self.assertEquals(2, item.sell_in)
        self.assertEquals(9, item.quality)

    def test_regular_decrease_by_one_at_last_day(self):
        item = Item("regular item", 1, 10)
        item.update_at_end_of_day()
        self.assertEquals(0, item.sell_in)
        self.assertEquals(9, item.quality)

    def test_regular_decreases_by_two_when_expired(self):
        item = Item("regular item", 0, 10)
        item.update_at_end_of_day()
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(8, item.quality)
        
    def test_regular_decreases_by_two_after_expiration(self):
        item = Item("regular item", -5, 10)
        item.update_at_end_of_day()
        self.assertEquals(-6, item.sell_in)
        self.assertEquals(8, item.quality)

    def test_regular_quality_not_negative(self):
        item = Item("regular item", 0, 1)
        item.update_at_end_of_day()
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)


if __name__ == '__main__':
    unittest.main()

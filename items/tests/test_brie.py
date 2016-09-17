# -*- coding: utf-8 -*-
import unittest

from items import Brie
from items import Item


class BrieTest(unittest.TestCase):
    def test_brie_quality_increases_by_one(self):
        item = Brie(3, 10)
        item.update_at_end_of_day()
        self.assertEquals("Aged Brie", item.name)
        self.assertEquals(2, item.sell_in)
        self.assertEquals(11, item.quality)

    # TODO: Is that a bug? Reading the spec carefully seems like quality should be increased by one, not two
    def test_brie_quality_increases_by_two_when_expired(self):
        item = Brie(0, 10)
        item.update_at_end_of_day()
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(12, item.quality)

    def test_brie_quality_not_higher_than_fifty(self):
        item = Brie(5, 49)
        item.update_at_end_of_day()
        self.assertEquals(Item._MAX_QUALITY, item.quality)
        item.update_at_end_of_day()
        self.assertEquals(Item._MAX_QUALITY, item.quality)

    def test_brie_quality_not_higher_than_fifty_when_expired(self):
        item = Brie(0, 49)
        item.update_at_end_of_day()
        self.assertEquals(Item._MAX_QUALITY, item.quality)
        item.update_at_end_of_day()
        self.assertEquals(Item._MAX_QUALITY, item.quality)


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock

from gilded_rose import GildedRose
from items import Item


class GildedRoseTest(unittest.TestCase):
    def test_empty_gilded(self):
        gilded_rose = GildedRose([])
        gilded_rose.update_quality()
        self.assertEquals([], gilded_rose.items)

    def test_gilded_single_item(self):
        item = Mock(return_value=Item("Iron man Battery", 8, 50))
        gilded_rose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEquals(1, len(gilded_rose.items))
        item.update_at_end_of_day.assert_called_once_with()

    def test_gilded_multiply_items(self):
        item1 = Mock(return_value=Item("Iron man Battery", 10, 50))
        item2 = Mock(return_value=Item("Milk", 3, 5))
        gilded_rose = GildedRose([item1, item2])
        gilded_rose.update_quality()
        self.assertEquals(2, len(gilded_rose.items))
        item1.update_at_end_of_day.assert_called_once_with()
        item2.update_at_end_of_day.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()

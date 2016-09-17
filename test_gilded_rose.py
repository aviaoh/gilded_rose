# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_regular_decrease_by_one(self):
        items = [Item("regular item", 3, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("regular item", items[0].name)
        self.assertEquals(2, items[0].sell_in)
        self.assertEquals(9, items[0].quality)

    def test_regular_decreases_by_two_when_expire(self):
        items = [Item("regular item", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(8, items[0].quality)

    def test_regular_quality_not_negative(self):
        items = [Item("regular item", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

    def test_brie_quality_increases_by_one(self):
        items = [Item("Aged Brie", 3, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(2, items[0].sell_in)
        self.assertEquals(11, items[0].quality)

    # TODO: Is that a bug? Reading the spec carefully seems like quality should be increased by one, not two
    def test_brie_quality_increases_by_two_when_expire(self):
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(12, items[0].quality)

    def test_brie_quality_not_higher_than_fifty(self):
        items = [Item("Aged Brie", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_brie_quality_not_higher_than_fifty_when_expire(self):
        items = [Item("Aged Brie", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_sulfuras_no_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 17)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(5, items[0].sell_in)
        self.assertEquals(17, items[0].quality)

    def test_backstage_quality_increases_by_one_when_more_than_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 17)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19, items[0].sell_in)
        self.assertEquals(18, items[0].quality)

    def test_backstage_quality_not_higher_than_fifty_when_more_than_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(19, items[0].sell_in)
        self.assertEquals(50, items[0].quality)

    def test_backstage_quality_increases_by_two_when_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 17)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(19, items[0].quality)

    def test_backstage_quality_not_higher_than_fifty_when_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(50, items[0].quality)

    def test_backstage_quality_increases_by_two_when_less_than_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 17)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(7, items[0].sell_in)
        self.assertEquals(19, items[0].quality)

    def test_backstage_quality_not_higher_than_fifty_when_less_than_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(7, items[0].sell_in)
        self.assertEquals(50, items[0].quality)

    def test_backstage_quality_increases_by_three_when_five_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 17)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(4, items[0].sell_in)
        self.assertEquals(20, items[0].quality)

    def test_backstage_quality_not_higher_than_fifty_when_five_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(4, items[0].sell_in)
        self.assertEquals(50, items[0].quality)

    def test_backstage_quality_increases_by_three_when_less_than_five_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 17)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(20, items[0].quality)

    def test_backstage_quality_not_higher_than_fifty_when_less_than_five_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(50, items[0].quality)

    def test_backstage_quality_zeroes_when_expire(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

    # def test_conjured_quality_decrease_by_two(self):
    #     items = [Item("Conjured", 8, 49)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals(7, items[0].sell_in)
    #     self.assertEquals(47, items[0].quality)
    #
    # def test_conjured_quality_decrease_by_four_when_expire(self):
    #     items = [Item("Conjured", 0, 49)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals(-1, items[0].sell_in)
    #     self.assertEquals(45, items[0].quality)

if __name__ == '__main__':
    unittest.main()

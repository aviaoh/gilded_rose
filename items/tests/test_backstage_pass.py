# -*- coding: utf-8 -*-
import unittest

from items import BackstagePass
from items import Item


class BackstagePassTest(unittest.TestCase):
    def test_backstage_quality_increases_by_one_when_more_than_ten_days(self):
        item = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 20, 17)
        item.update_at_end_of_day()
        self.assertEquals(19, item.sell_in)
        self.assertEquals(18, item.quality)

    def test_backstage_quality_not_higher_than_fifty_when_more_than_ten_days(self):
        item = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 20, 49)
        item.update_at_end_of_day()
        self.assertEquals(19, item.sell_in)
        self.assertEquals(Item._MAX_QUALITY, item.quality)

    def test_backstage_quality_increases_by_two_when_ten_days(self):
        item = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 10, 17)
        item.update_at_end_of_day()
        self.assertEquals(9, item.sell_in)
        self.assertEquals(19, item.quality)

    def test_backstage_quality_not_higher_than_fifty_when_ten_days(self):
        item = BackstagePass("Backstage passes to a L60ETC concert", 10, 49)
        item.update_at_end_of_day()
        self.assertEquals(9, item.sell_in)
        self.assertEquals(Item._MAX_QUALITY, item.quality)

    def test_backstage_quality_increases_by_two_when_less_than_ten_days(self):
        item = BackstagePass("Backstage passes to a L80ETC concert", 8, 17)
        item.update_at_end_of_day()
        self.assertEquals(7, item.sell_in)
        self.assertEquals(19, item.quality)

    def test_backstage_quality_not_higher_than_fifty_when_less_than_ten_days(self):
        item = BackstagePass("Backstage passes to a L10TC concert", 8, 49)
        item.update_at_end_of_day()
        self.assertEquals(7, item.sell_in)
        self.assertEquals(Item._MAX_QUALITY, item.quality)

    def test_backstage_quality_increases_by_three_when_five_days(self):
        item = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 5, 17)
        item.update_at_end_of_day()
        self.assertEquals(4, item.sell_in)
        self.assertEquals(20, item.quality)

    def test_backstage_quality_not_higher_than_fifty_when_five_days(self):
        item = BackstagePass("Backstage passes to a L10TC concert", 5, 49)
        item.update_at_end_of_day()
        self.assertEquals(4, item.sell_in)
        self.assertEquals(Item._MAX_QUALITY, item.quality)

    def test_backstage_quality_increases_by_three_when_less_than_five_days(self):
        item = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 2, 17)
        item.update_at_end_of_day()
        self.assertEquals(1, item.sell_in)
        self.assertEquals(20, item.quality)

    def test_backstage_quality_not_higher_than_fifty_when_less_than_five_days(self):
        item = BackstagePass("Backstage passes to a L60ETC concert", 1, 49)
        item.update_at_end_of_day()
        self.assertEquals(0, item.sell_in)
        self.assertEquals(Item._MAX_QUALITY, item.quality)

    def test_backstage_quality_zeroes_when_expired(self):
        item = BackstagePass("Backstage passes to a L80ETC concert", 0, 49)
        item.update_at_end_of_day()
        self.assertEquals(-1, item.sell_in)
        self.assertEquals(0, item.quality)

        if __name__ == '__main__':
            unittest.main()

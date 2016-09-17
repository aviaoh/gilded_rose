# -*- coding: utf-8 -*-
import unittest

from items import Sulfuras


class SulfurasTest(unittest.TestCase):
    def test_sulfuras_no_changes(self):
        item = Sulfuras(5, 17)
        item.update_at_end_of_day()
        self.assertEquals("Sulfuras, Hand of Ragnaros", item.name)
        self.assertEquals(5, item.sell_in)
        self.assertEquals(17, item.quality)


if __name__ == '__main__':
    unittest.main()

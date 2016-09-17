from items.item import Item


class BackstagePass(Item):
    def _get_change_in_quality(self):
        if self._is_expired():
            return -self.quality
        elif self.sell_in > 10:
            return 1
        elif self.sell_in > 5:
            return 2
        else:
            return 3

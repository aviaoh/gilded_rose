from items.item import Item


class Brie(Item):
    def __init__(self, sell_in, quality):
        super(Brie, self).__init__("Aged Brie", sell_in, quality)

    def _get_change_in_quality(self):
        return 2 if self._is_expired() else 1

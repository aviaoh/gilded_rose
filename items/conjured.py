from items.item import Item


class Conjured(Item):
    def _get_change_in_quality(self):
        return 2 * super(Conjured, self)._get_change_in_quality()

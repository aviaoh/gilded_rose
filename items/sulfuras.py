from items.item import Item


class Sulfuras(Item):
    def __init__(self, sell_in, quality):
        super(Sulfuras, self).__init__("Sulfuras, Hand of Ragnaros", sell_in, quality)

    def update_at_end_of_day(self):
        pass

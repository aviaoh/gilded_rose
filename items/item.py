class Item:
    _MAX_QUALITY = 50
    _MIN_QUALITY = 0

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        assert quality >= Item._MIN_QUALITY and quality <= Item._MAX_QUALITY, \
            "Invalid quality value. Please provide value between " + str(Item._MIN_QUALITY) + " to " + str(Item._MAX_QUALITY)
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_at_end_of_day(self):
        self.__update_sell_in()
        self.__update_quality()

    def __update_sell_in(self):
        self.sell_in -= 1

    def __update_quality(self):
        self.quality = min(Item._MAX_QUALITY, max(Item._MIN_QUALITY, self.quality + self._get_change_in_quality()))

    def _get_change_in_quality(self):
        return -2 if self._is_expired() else -1

    def _is_expired(self):
        return self.sell_in < 0

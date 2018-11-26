from __future__ import division
import time


class Flower(object):
    def __init__(self, name, price, color, stalk_length, time_of_life):
        self._name = name
        Flower.check(price)
        self._price = price
        self._color = color
        Flower.check(stalk_length)
        self._stalk_length = stalk_length
        Flower.check(time_of_life)
        self._time_of_life = time_of_life
        self._time_of_withering = time.time() + self._time_of_life

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        Flower.check(price)
        self._price = price

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def stalk_length(self):
        return self._stalk_length

    @stalk_length.setter
    def stalk_length(self, stalk_length):
        Flower.check(stalk_length)
        self._stalk_length = stalk_length

    @property
    def time_of_life(self):
        return self._time_of_life

    @time_of_life.setter
    def time_of_life(self, time_of_life):
        Flower.check(time_of_life)
        self._time_of_life = time_of_life

    @property
    def time_of_withering(self):
        return self._time_of_withering

    @staticmethod
    def check(value):
        if not isinstance(value, (float, int)):
            raise TypeError("Type should be int or float. Except got type: {}".format(type(value)))
        if value <= 0:
            raise ValueError("Value should be positive number. Except got value: {}".format(value))

    def __str__(self):
        return "Flower name: {}\n price: {}\n color: {}\n stalk length: {}\n time of withering: {}\n".format(
            self._name, self._price, self._color, self._stalk_length,
            time.strftime('%d:%m:%Y %H:%M:%S', time.localtime(self._time_of_withering))
        )


class Tulip(Flower):
    def __init__(self, price, color, stalk_length, time_of_life):
        name = "Tulip"
        super(Tulip, self).__init__(name, price, color, stalk_length, time_of_life)


class Rose(Flower):
    def __init__(self, price, color, stalk_length, time_of_life):
        name = "Rose"
        super(Rose, self).__init__(name, price, color, stalk_length, time_of_life)


class Pion(Flower):
    def __init__(self, price, color, stalk_length, time_of_life):
        name = "Pion"
        super(Pion, self).__init__(name, price, color, stalk_length, time_of_life)


class Lavender(Flower):
    def __init__(self, price, color, stalk_length, time_of_life):
        name = "Lavender"
        super(Lavender, self).__init__(name, price, color, stalk_length, time_of_life)


class Chamomile(Flower):
    def __init__(self, price, color, stalk_length, time_of_life):
        name = "Chamomile"
        super(Chamomile, self).__init__(name, price, color, stalk_length, time_of_life)


class Bouquet(object):
    def __init__(self):
        self._bouquet = []

    def add_flower(self, flower, count=1):
        if not isinstance(flower, Flower):
            raise TypeError("In bouquet you can add only Flower objects. Except got type: {}".format(type(flower)))
        self._bouquet.extend([flower for _ in range(count)])

    def add_flowers(self, *flowers):
        for flower in flowers:
            self.add_flower(flower)

    def remove_flower(self, flower):
        try:
            self._bouquet.remove(flower)
        except ValueError:
            print("ValueError: flower is not in bouquet".format(flower))

    def remove_flowers(self, *flowers):
        for flower in flowers:
            self.remove_flower(flower)

    def calculate_price(self):
        return sum(flower.price for flower in self._bouquet)

    def calculate_time_of_withering(self):
        return sum(flower.time_of_withering for flower in self._bouquet) / len(self._bouquet)

    def sort_by_price(self, reverse=False):
        self._bouquet.sort(key=lambda x: x.price, reverse=reverse)

    def sort_by_stalk_length(self, reverse=False):
        self._bouquet.sort(key=lambda x: x.stalk_length, reverse=reverse)

    def sort_by_color(self, reverse=False):
        self._bouquet.sort(key=lambda x: x.color, reverse=reverse)

    def sort_by_freshness(self, reverse=True):
        self._bouquet.sort(key=lambda x: x.time_of_withering, reverse=reverse)

    def contains(self, flower):
        if flower in self._bouquet:
            return True
        else:
            return False

    def search_by_price(self, start_price, end_price=None):
        if end_price is not None:
            return [flower for flower in self._bouquet if start_price <= flower.price <= end_price]
        else:
            return [flower for flower in self._bouquet if start_price <= flower.price]

    def search_by_color(self, color):
        return [flower for flower in self._bouquet if flower.color == color]

    def search_by_stalk_length(self, start_length, end_length=None):
        if end_length is not None:
            return [flower for flower in self._bouquet if start_length <= flower.stalk_length <= end_length]
        else:
            return [flower for flower in self._bouquet if start_length <= flower.stalk_length]

    def __iter__(self):
        return iter(self._bouquet)

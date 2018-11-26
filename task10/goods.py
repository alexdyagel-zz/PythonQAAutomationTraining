from __future__ import division


class Goods(object):
    MAX_PERCENTAGE = 100
    MIN_PERCENTAGE = 0

    def __init__(self, price):
        self._price = price
        self._discount = 0
        self._freeze = False
        self._discounted_price = self._price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if self._freeze:
            raise AttributeError("You cant change price because it is freezed.")
        if not isinstance(price, (float, int)):
            raise TypeError("Price should be int or float number. Except got type: {}".format(type(price)))
        if price <= 0:
            raise ValueError("Price should be positive number. Except got value: {}".format(price))
        self._price = price

    @property
    def discounted_price(self):
        return self._price - (self._price * (self._discount / Goods.MAX_PERCENTAGE))

    def set_discount(self, discount):
        if self._freeze:
            raise AttributeError("You cant apply discount because price is freezed.")
        if not isinstance(discount, (float, int)):
            raise TypeError("Discount should be int or float number. Except got type: {}".format(type(discount)))
        if discount < Goods.MIN_PERCENTAGE or discount > Goods.MAX_PERCENTAGE:
            raise ValueError("Discount should be from 0 to 100%. Except got : {}".format(discount))
        self._discount = discount

    def reset_discount(self):
        if self._freeze:
            raise AttributeError("You cant apply discount because price is freezed.")
        self._discount = 0

    def freeze_price(self, freeze=True):
        self._freeze = freeze


class Tools(Goods):
    def __init__(self, price):
        super(Tools, self).__init__(price)


class Food(Goods):
    def __init__(self, price):
        super(Food, self).__init__(price)


class Carrot(Food):
    def __init__(self, price):
        super(Carrot, self).__init__(price)


class Selery(Food):
    def __init__(self, price):
        super(Selery, self).__init__(price)


class Pomelo(Food):
    def __init__(self, price):
        super(Pomelo, self).__init__(price)


class Pork(Food):
    def __init__(self, price):
        super(Pork, self).__init__(price)


class Hammer(Tools):
    def __init__(self, price):
        super(Hammer, self).__init__(price)


class Pliers(Tools):
    def __init__(self, price):
        super(Pliers, self).__init__(price)


class Fretsaw(Tools):
    def __init__(self, price):
        super(Tools, self).__init__(price)


class Drill(Tools):
    def __init__(self, price):
        super(Drill, self).__init__(price)

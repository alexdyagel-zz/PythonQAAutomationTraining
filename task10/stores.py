import abc
import goods

ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()})


class Store(ABC):

    def __init__(self):
        self.assortment = []

    @abc.abstractmethod
    def add_item(self, item):
        pass

    @abc.abstractmethod
    def add_items(self, *items):
        pass

    def remove_item(self, item):
        try:
            self.assortment.remove(item)
        except ValueError:
            print("ValueError: Item is not in store".format(item))

    def remove_items(self, *items):
        for el in items:
            try:
                self.assortment.remove(el)
            except ValueError:
                print("ValueError: Item is not in store".format(el))

    def calculate_overall_price_without_discount(self):
        summed_price = 0
        for good in self.assortment:
            summed_price += good.price
        return summed_price

    def calculate_overall_price_with_discount(self):
        summed_price = 0
        for good in self.assortment:
            summed_price += good.discounted_price
        return summed_price


class GroceryStore(Store):

    def __init__(self):
        super(GroceryStore, self).__init__()

    def add_item(self, item):
        if not isinstance(item, goods.Food):
            raise TypeError("In GroceryStore you can add only Food objects. Except got type: {}".format(type(item)))
        self.assortment.append(item)

    def add_items(self, *items):
        for item in items:
            if not isinstance(item, goods.Food):
                raise TypeError("In GroceryStore you can add only Food objects. Except got type: {}".format(type(item)))
        self.assortment.extend(items)


class HardwareStore(Store):
    def __init__(self):
        super(HardwareStore, self).__init__()

    def add_item(self, item):
        if not isinstance(item, goods.Tools):
            raise TypeError("In HardwareStore you can add only Tools objects. Except got type: {}".format(type(item)))
        self.assortment.append(item)

    def add_items(self, *items):
        for item in items:
            if not isinstance(item, goods.Tools):
                raise TypeError(
                    "In HardwareStore you can add only Tools objects. Except got type: {}".format(type(item)))
        self.assortment.extend(items)

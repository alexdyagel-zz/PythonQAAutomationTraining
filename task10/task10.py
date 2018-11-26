from goods import *
from stores import GroceryStore, HardwareStore

selery = Selery(25)
drill = Drill(125)
pomelo = Pomelo(10)
pomelo1 = Pomelo(15)
fretsaw = Fretsaw(123)
fretsaw1 = Fretsaw(125)
fretsaw.set_discount(55)
fretsaw1.set_discount(65)

grocery_store = GroceryStore()
tools_store = HardwareStore()
tools_store1 = HardwareStore()
tools_store.add_item(drill)
tools_store1.add_items(fretsaw, fretsaw1)

print("Price with discount: {}".format(tools_store1.calculate_overall_price_with_discount()))
print("Price without discount: {}".format(tools_store1.calculate_overall_price_without_discount()))

Using your knowledge about class attributes operators:

1.      Make a class “Store”.

2.      Inherit two classes from it – “GroceryStore” and “HardwareStore”.

3.      Create a class “Goods”, inherit classes “Food” and “Tools” from it.

4.      Subclass 4 random food and tools naming from each (Banana, Apple, Ham - from Food, Nail, Axe, Saw – from Tools…).

5.      Each of the goods’ object must have a read-write “price” attribute, which is set upon creation (make the price up, just should be a positive int or float), set_discount() method that takes discount percentage as an argument, reset_discount() that typically sets it to 0.

6.      Goods objects must also possess freeze_price() method that takes Boolean value as an argument and allows changing price or discount if it was called with True only. By default price is not frozen. You can allow changing the values for example, after banana.freeze_price(False) called. If banana.freeze_price(True) is called, the price should not change.

7.      Instantiate one grocery store and two hardware stores, they all must have methods:

8.      add_item(item) and add_items(*items)

9.      remove_item(item) and remove_items(*items). Allow optional count argument to define how many items are going to be added.

10.   calculate overall goods price currently available (without discount)

11.   calculate overall goods price currently available (with discount)

12.   Shops must allow adding goods of their supported types only – Grocery stores accept goods of Food type only, Hardware stores can add Tools only.
TypeError must be raised for incompatible items.

13.   Shops allow having same goods of different prices, mind that.

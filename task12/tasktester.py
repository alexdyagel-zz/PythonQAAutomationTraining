from flowers import *

a = Pion(4, "red", 10, 5500000)
b = Tulip(60, "yellow", 15, 55)
c = Rose(55, "green", 20, 255)
d = Chamomile(123, "red", 40, 55)
e = Lavender(9, "white", 30, 50005)
bouquet = Bouquet()
bouquet.add_flowers(a, b, c, d, e)

for flower in bouquet:
    print(flower)

print("-------------------------")
print("Sorted by price:")
print("-------------------------")
bouquet.sort_by_price(reverse=True)
for flower in bouquet:
    print(flower)

print("-------------------------")
print("Sorted by freshness:")
print("-------------------------")
bouquet.sort_by_freshness(reverse=True)
for flower in bouquet:
    print(flower)

print("-------------------------")
print("Sorted by color:")
print("-------------------------")
bouquet.sort_by_color(reverse=False)
for flower in bouquet:
    print(flower)

print("-------------------------")
print("Sorted by stalk length:")
print("-------------------------")
bouquet.sort_by_stalk_length(reverse=False)
for flower in bouquet:
    print(flower)

color = "green"
print("-------------------------")
print("Search {} color:".format(color))
print("-------------------------")
searched = bouquet.search_by_color(color)
for flower in searched:
    print(flower)

from_ = 25
to = 250
print("----------------------------")
print("Search price from {} to {}:".format(from_, to))
print("-----------------------------")
searched = bouquet.search_by_price(from_, to)
for flower in searched:
    print(flower)

from_ = 10
to = 25
print("-----------------------------------")
print("Search stack length from {} to {}:".format(from_, to))
print("------------------------------------")
searched = bouquet.search_by_stalk_length(from_, to)
for flower in searched:
    print(flower)

print("total price of bouquet: {}".format(bouquet.calculate_price()))
print("time of withering of bouquet: {}".format(time.strftime('%d:%m:%Y %H:%M:%S',
                                                              time.localtime(
                                                                  bouquet.calculate_time_of_withering()))))

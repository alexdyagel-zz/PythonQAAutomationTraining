# author: Alex Dyagel

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
email = "as.dyagel@gmail.com"
text += email

print("=" * 60)
print("Number of symbols in text: ")
print(len(text))


def get_number_of_vowels(sometext):
    vowels = ["a", "e", "i", "o", "u", "y"]
    vowels_in_text = 0
    for symbol in sometext:
        if symbol.lower() in vowels:
            vowels_in_text += 1
    return vowels_in_text


print("=" * 60)
print("Number of vowels in text: ")
print(get_number_of_vowels(text))

print("=" * 60)
first_18_symbol = 17
step = 18
each_18_symbol = text[first_18_symbol::step]
modified = [symbol.swapcase() for symbol in each_18_symbol]

number = 18
for symbol in modified:
    print(str(number) + symbol)
    number += 18

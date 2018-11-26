import itertools as it

zen = """Beautiful is better than ugly.
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


def print_table(list_, limit_=-1):
    if limit_:
        print('\n'.join("{}={}".format(k, v) for (k, v) in list_[:limit_:]))
    else:
        print('\n'.join("{}={}".format(k, v) for (k, v) in list_[::]))


def print_flipped_table(list_, limit_=-1):
    if limit_ <= -1:
        print('\n'.join("{}={}".format(v, k) for (k, v) in list_[::]))
    else:
        print('\n'.join("{}={}".format(v, k) for (k, v) in list_[:limit_:]))


def count_letter_in_string(letter, text):
    return letter, text.count(letter)


def get_number_of_letters_meeting(text):
    A_dec = 65
    Z_dec = 90
    a_dec = 97
    z_dec = 122
    letters_meeting_set = \
        [count_letter_in_string(chr(letter_dec), text) for letter_dec in
         it.chain(range(A_dec, Z_dec + 1), range(a_dec, z_dec + 1))]
    return letters_meeting_set


def get_sorted_by_frequency_list_(letters_meeting_):
    return sorted(letters_meeting_, key=lambda tup: tup[1], reverse=True)


def get_sorted_by_alphabet_list_(letters_meeting_):
    return sorted(letters_meeting_, key=lambda tup: tup[0])


print("=" * 60)
print("Meetings of each letter in text (already sorted by alphabet):")
letters_meeting = get_number_of_letters_meeting(zen)
print_table(letters_meeting)

print("=" * 60)
print("Meetings sorted by frequency count:")
letters_meeting = get_sorted_by_frequency_list_(letters_meeting)
print_table(letters_meeting)

print("=" * 60)
limit = 20
print("Top", limit, "frequent meetings:")
print_table(letters_meeting, limit)

print("=" * 60)
print("Meetings sorted by alphabet and FLIPPED:")
letters_meeting = get_sorted_by_alphabet_list_(letters_meeting)
print_flipped_table(letters_meeting)


Create a function “arange” that duplicates “xrange” in Python2, but can handle <long> numeric type.

It should  support positional arguments, negative numbers for any of the argument, just like xrange does.

The function must be implemented as a generator, avoid any non-lazy iterable return types like lists, tuples, sets or what not.

g = arange(1000000000000000000000000000000000000000000000000000000000000000000000)

g = arange(30L, 2)

g = arange(8, 2, -3L)

g = arange(9, 999, 7)

g à <generator object g at 0x000001AD9F53DD58>

type(g) à generator

etc…

 

To unpack generator, use <for _ in gen> loop, or convert it to a tuple, list or other iterable.

You may not implement certain cases of negative stepping, etc., but the main requirement is that the function must not hang or 
stuck in an infinite loop in any case.

At the very least, I must see a warning that such case is not allowed/not supported. If so, it would be nice of you to 
list the scenarios not supported or implemented yet.

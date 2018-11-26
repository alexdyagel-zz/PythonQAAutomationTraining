Make the code work without exceptions raised.

The task is similar to the one with the long_long_function() function.
Implement “threaded_execution” decorator so that every call of a decorated function gets called in a separate thread.
This must lead to overall run time reduction, in comparison to linear code -> this will make the last assertion to pass successfully.

 

*extra task

Create a function that accepts a filename. Let’s suppose the file exists and contains some code.

Your function should check whether the parenthesis are consistent, all opened parenthesis have their closing part, i.e. {([])}

** Mind cases when parenthesis are unaligned or misplaced, though they have closing pairs. i.e. {[(])}

*** Let the checking function print summary, and if there is an error, report line number and char offset of first found misplaced parenthesis.

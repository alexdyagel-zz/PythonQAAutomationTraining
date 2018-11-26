Using exceptions handling, create a script that prints out current time every 1 minute in an infinite loop.

When Ctrl-C is pressed (KeyboardInterrupt exception), the script must handle the exception, and print out the number of 
attempts left to exit (3 by default), and decrement the attempts counter. When the counter get to 0, the script must prompt 
for a choice “Are you sure you want to exit? y/N” using input function and decrement the counter only if “Y/y” is provided.
 

1) Write a wrapper for the os.walk() function that returns a generator.
The generator should give me all the files (and only files, excluding directories!) with their absolute path.

Example:


import os

files_lazy_lister = your_wrapper(os.walk("c:\\"))
list(files_lazy_lister)


output example =>
["C:\\Development\\ARM Embedded Toolchain\\5.4 2016q3\\uninstall.exe",
"C:\\Development\\ARM Embedded Toolchain\\5.4 2016q3\\arm-none-eabi\\bin\\ar.exe",
"C:\\Development\\ARM Embedded Toolchain\\5.4 2016q3\\arm-none-eabi\\bin\\as.exe",
"C:\\Windows\\bfsvc.exe",
"C:\\Windows\\explorer.exe", ...]

 

2) Make the same function optionally parametrized, let it accept minimal size (in kb) for the files to list:
Sized files’ param

files_lazy_lister = your_wrapper(os.walk("c:\\"), min_size_kb=100)

list(files_lazy_lister)

output example =>
["C:\\Windows\\bfsvc.exe",
"C:\\Windows\\explorer.exe", ...]

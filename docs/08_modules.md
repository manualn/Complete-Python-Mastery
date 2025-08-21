# Creating Modules

Till the last programs, all coding
was done in one file, but that's
not how real programs are built.  
Because a real program contains
tens or thousands of lines of codes. 
It is like going to supermarket
without sections, so that it will
be difficult to find products. 
This same concept is used in programming.  
So as the program
grows, split the code across
multiple files.  
Refer each file as module. So
module is a file that contains some python code

Each module should contain highly related object. These objects contain objects, classes, variables and so on

- To do the seperation of different functions into different files

easily:
```python
# 79_creating_modules.py
from sales import cale_chipping
```
![syntax demo](/images/79_creating_modules.png)

Also we can import calculate tax
and then call it
```python
# 79_creating_modules.py
from sales import calc_shipping, calc_tax
calc_shipping()
calc_taxi()
```

There is another way to import:
```python
# 79_creating_modules.py
import sales
sales.calc_shipping()
```

Its your personal preference to choose which method. There is no right or wrong here.

# Compiled Python Files
Compiling of these files will speed up the loading of this module. It does not alter the actual performance of this application.  
To know that the compiled version is uptodate with the latest code in the sales module, It checks the date and time of the two files compiled.  
Here the file is compiled using cpython version 37.  
In this python byte code is used:
![syntax demo](/images/80_compiled_python_files.png)
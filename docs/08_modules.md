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


# Module Search Path

Import sales from the first section. Python will look for a file
called sales.py in the current directory. If it is not found in
current, it will search for it in a bunch of predefined directories

→ There is a built-in module called path

```python
# 80_module_search_path.py
import sales
import sys
print(sys.path)
```

If we run the above code, the result will be an array of strings.
The first element in this array represents the current folder.
It will be different in different machines.

After that 3 frameworks ie, python version framework. This is also
different on your machine depending on operating system

When python sees an import statement, it will search all these
directories to find this module


# Packages

→ Python modules in one folder is not good

→ Here we will move this sales modules to a directory called commerce. So add the sub directory called ecommerce and then drag and drop this sales module into ecommerce

→ Add a new file called __init__.py

→ When this new file is added, python treats the commerce folder as package

→ A package is a container for one or more modules

In technical terms, the package is mapped to a directory and a module is mapped to file.

```python
# 81_packages.py
import ecommerce.sales

ecommerce.sales.calc_tax()
```

This makes our code little tedious.

For avoiding that we can use from statement

```python
# 81_packages.py
from ecommerce.sales import calc_tax

calc_tax()
```
Also we can import sales module as an object and then use operator to access all the members of this module.
![syntax demo](/images/81_packages_screenshot.png)


# Subpackages

As a program grows bigger, break a package into sub packages.

For example ecommerce package can be broken down into few sub packages. For that add new folder into ecommerce named shopping and move sales module into this folder.

Here shopping is not a package because there is no init file. So add init file in a shopping folder.

```python
# 82_subpackages.py
from ecommerce_82_subpackages.shopping import sales
sales.calc_chipping()
```


# Intra-package References

Add a sub package called customer in ecommerce package.
In customer package, create a contact file.  
Absolute import can be used to import contact from customer

```python
# 83_intra_package_references.py
from ecommerce_83_intra_package_references.customer import contact
```

We can also use a relative import. Here we are at the ecommerce
package level, in this package there are two subpackages – customer
and shopping

```python
# 83_intra_package_references.py
from ..customer import contact
```

Prefer to use absolute imports — that is recommended by PEP 8.


# The dir Function

Here we are going to look at a powerful built-in function called dir.

This function helps to get the list of attributes and methods in an object

```python
# 84_the_dir_function.py
from ecommerce.shopping import sales
sales.
```

dot operator is used to access all the attributes and functions defined in it

You can use dir function for debugging

```python
# 84_the_dir_function.py
print(dir(sales))
```

Result of this program will be an array of strings. In this array we have all attributes and methods to find an object.

In sales function we have shipping and tax as attributes as well as magic attributes are automatically created.

- list out some of them

```python
# 84_the_dir_function.py
print(sales.__name__)
print(sales.__package__)
print(sales.__file__)
```

- Name of module, name of packages, and path to the file and file system is printed by running the above code


# Executing modules as scripts

→ In the last section we have defined sales module that have two functions

```python
# 85_executing_modules_as_scripts.py
print("Sales Initialized")
def calc_tax():
    pass
def calc_shipping():
    pass
```

→ If this module is imported in a few modules of our program, python will load it only once, and then cache it in memory.

So the statements are written, it will be executed

Using the same technique you can write the initialization code for our packages

```python
# 85_executing_modules_as_scripts.py
print("Ecommerce Initialized")
```

Run this program in `__init__` file and you can see the result.

From the last module, you know that every module has a built-in name attribute that is automatically created

```python
# 85_executing_modules_as_scripts.py
print("Sales Initialized", __name__)
```

If you run this program in sales module, the name of our module is changed to main

So the name of the module that starts our program is always main

With the above code we can make the sales file usable as script and also used as a module.

```python
# 85_executing_modules_as_scripts.py
if __name__ == "__main__":
    print("sales started")
    calc_tax()
```

So if you run this module directly, the name of our module will be `__main__`.

If we import this to another module, this code will not be executed. The name of this module will no longer be `__main__`. It will be `ecommerce`.


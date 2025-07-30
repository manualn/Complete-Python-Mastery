# Classes

This is extremely important part in python programming.
Every list object in python has these methods
![syntax demo](/images/45_classes_example.png)

we can create objects and this object would have methods like add, remove, get total etc.
Example:
```python
# 45_classes_examples.py
shopping_cart.add()
shopping_cart.remove()
shopping_cart.get_total()
```
Also we could have a point object with methods like draw, move, or get distance etc.
```python
# 45_classes_examples.py
point.draw()
point.move()
point.get_distance()
```
Class is a blue print for creating new objects
Throughout the course you have heard about class.  
For example  
x = 1  
print(type(x))

Certain terms to be studied in this section.

class: blueprint for creating new objects  
Object: instance of a class.

Example:  
Class: Human  
Objects: John, Mary, Jack


# Creating classes

- Here we are going to create a point class within python.
- Pascal naming convention is used here.
- To name variables and functions use all lower case letters and use underscore to seperate multiple words.
- But to name classes different convention is used which is called pascal naming convention such that first letter of every word should be uppercase and shouldn't use underscore.

Eg: 
```python
# 46_creating_classes.py
class MyPoint
```
- Add colon to indicate a block - And in this block all functions related to points written here.

Example:
```python
# 46_creating_classes.py
class Point:
    def draw(self):
        print("draw")
```

Here in the above case we define a function called draw.  
All functions in classes have one parameter and is called parameter self.  

If you use dot operator you can see draw method and a bunch of other methods.
![syntax demo](/images/46_creating_classes.png)

```python
# 46_creating_classes.py
point = Point()
print(type(point))
```
- Output of the above code you will get the output as class 'main.Point'
- The main in the output is the name of module  
- Another function called isinstance function used to know if an object is an instance of a given class
```python
# 46_creating_class.py
print(isinstance(point, Point))
```
- When you run the above code you will get true


# Constructors

Continuing the code from last section

```python
# 47_constructors.py
class Point:
    def draw(self):
        print("draw")

point = Point(1, 2)
```

Constructor is a special method that is called to view point object

Now we will learn to create a constructor
Here we are defining a new function.

```python
# 47_constructors.py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(1, 2)
print(point.x)
```

__init__ is a special method that we call a magic method.
There are several magic methods which will be explained in coming sessions
This magic method is called a constructor and it's executed when a new point object is created

- self is reference to current point object
- Here we can have attributes like x and y, that can be easily print on terminals
- set self.x = x and self.y = y and when you use dot operator x and y will be there.

Now back to draw function.
Here using self, you can read attributes of the current object or you can call other methods in this object

```python
# 47_constructors.py
def draw(self):
    print(f"Point ({self.x}, {self.y})")

point.draw(point)
```

The methods that we define in a class should have at least one parameter, which be reference is called self


# Class vs Instance Attributes

Whenever you create a new point object, it will have these attributes by default.  
So here we can set point.z = 10 because objects in python are dynamic. In python we don't have to define all the attributes in constructor

```python
# 48_class_vs_instance_attributes.py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Point({self.x}, {self.y})")

point = Point(1, 2)
point.z = 10
point.draw()
```

Here we defined x, y, z attributes, they are called instance attributes.

These are attributes that belong to point instances or point objects.  
Every point objects have different values for these attributes

Draw another point in terminal.

```python
# 48_class_vs_instance_attributes.py
another = Point(3, 4)
another.draw()
```

Now we can see two points and these are completely independent of each other.

Each point has it's own attribute.
Now we can look at class level attribute.

```python
# 48_class_vs_instance_attributes.py
class Point:
    default_color = "red"
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
```

Class attributes are shared across all instances of a class

If default color is changed to "yellow":

```python
# 48_class_vs_instance_attributes.py
Point.default_color = "yellow"
point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
```

Class reference is used here and not working with any point objects.
You can see after running code the colour has changed to yellow.
Similarly another also can be printed in this colour

```python
# 48_class_vs_instance_attributes.py
another = Point(3, 4)
print(another.default_color)
another.draw()
```


# Class vs Instance Methods

There are instance methods and class methods

```python
# 49_class_vs_instance_methods.py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print(f"Point({self.x}, {self.y})")
```

In the above example, both these examples defined in the point class are instance methods

Using an instance of the point class, use these instance methods whenever you need reference
If you don't really need an existing object, then class method can be used

For example:
```python
# 49_class_vs_instance_methods.py
point = Point(0, 0)
point = Point.zero()
point.draw()
```

In this case, zero is method that is defined at the class level and it will return a point object.
We refer to this zero method as factory method, because it's like a factory that creates a new object

```python
# 49_class_vs_instance_methods.py
point = Point(0, 0, 1, "an")
point = Point.zero()
point.draw()
```

The above is an example of initializing a complex one.

Now back to point class, define a method zero and call its parameter cls. To make this method a class method, we should decorate it with something like given below outside class method. This is what we call a decorator. It's a way of extending the behaviour of a method - this is what we call class method in python

```python
# 49_class_vs_instance_methods.py
@classmethod
def zero(cls):
    return cls(0, 0)
```


# Magic Methods

Throughout the course you have heard magic methods a few times.
These methods have two underscores at the beginning and end of their name, and are called automatically by python interpreter.

Here we have `__init__` magic method, which is automatically called by python not directly called by us.

To know more about magic methods. Search for python 3 magic methods or click on the link: [magic methods](https://rszalski.github.io/magicmethods/)

Back to our code

```python
# 50_magic_methods.py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"point ({self.x}, {self.y})")

point = Point(1, 2)
print(point)
```

If we print the point object on terminal, we get name of module followed by class name and address of the point object in memory

If str method is used:  
point.__str__

- This can be reimplimented in a better way.

```python
# 50_magic_methods.py
class Point:
    def __str__(self):
        return f"({self.x}, {self.y})"
point = Point(1, 2)
print(str(point))
```

- we get the result (1,2)

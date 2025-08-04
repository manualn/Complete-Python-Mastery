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


# Comparing Objects

There are situations where two objects can be compared.
Here we are comparing two point objects:

```python
# 51_comparing_objects.py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(1, 2)
other = Point(1, 2)
print(point == other)
```

We get False as the result. The reason you get False is by default this equality operator compares the references and addresses of these two objects in memory.  
In the above case, these two variables are referencing two different objects in memory and that's why it's not equal.

Magic method is used to solve this problem. This magic method is called when you compare two objects.  
You can go to the link given in the last chapter and in that page you will see comparison magic methods.
We have:
- "eq" for testing equality
- "ne" for inequality
- "lt" for less than
- "gt" for greater than

Now we are going to define "eq" magic method in the point class and it requires two parameters:

```python
# 51_comparing_objects.py
class Point:
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

point = Point(1, 2)
other = Point(1, 2)
print(point == other)
```

When we run the program we will get the result True.

If we run "print(point > other)" you'll get the type error because the greater than operator is not supported between instances of the point class.

To solve this problem, we need to define another magic method:

```python
# 51_comparing_objects.py
class Point:
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

point = Point(10, 20)
other = Point(1, 2)
print(point > other)
```

Let's run the program and the output will be True. If you change "print(point < other)", you will get the result False.


# Performing Arithmetic Operations

There are magic methods for performing arithmetic operations between two objects.
In the list of magic methods in the link mentioned in chapter magic methods, we have numeric magic methods.

```python
# 52_performing_arithmetic_operations.py
class Point:
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(combined.x)
```


# Making Custom Containers

We have studied many data structures like lists, sets etc in python.
There are times that you may need to create your own custom container types. Here we take tag cloud.
We know class represents a container, it supports various operators.

```python
# 53_making_custom_containers.py
cloud = TagCloud()
len(cloud)
cloud["python"] = 10
for tag in cloud:
    print(tag)
```

The above are operations supported in this custom container type.

Now we will look upon how to implement a class sentence:

```python
# 53_making_custom_containers.py
class TagCloud:
    def __init__(self):
        self.tags = {}
    
    def add(self, tag):
        self.tags[tag] = self.tags.get(tag, 0) + 1
```

In the above dictionary is used internally because it allows you to quickly get the numbers of given tags.

```python
# 53_making_custom_containers.py
cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)
```

Here instead of using a plain old dictionary, then a custom class is used because to make it a little bit smarter than a typical dictionary.

You can print it lower by adding tag.lower & instead of tag in brackets.

Now taking this to next level. Here magic method is used:

```python
# 53_making_custom_containers.py
def __getitem__(self, tag):
    return self.tags.get(tag.lower(), 0)

def __setitem__(self, tag, count):
    self.tags[tag.lower()] = count

def __len__(self):
    return len(self.tags)

def __iter__(self):
    return iter(self.tags)
    
cloud["python"] = 10
len(cloud)
```

In order to implement for loop we have to use another magic method called__iter__. This function returns an iterator object which gives one item at a time in for loop.


# Private Members

Tag cloud class built in the last lecture has some tiny issues.

```python
# 54_private_members.py
cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags["PYTHON"])
```

Here our program is going to crash when you run this you will get an exception of type key error because we don't have this key in dictionary.

In order to avoid this error, you should hide this attribute from the outside.

Back to our class code, make some changes. all tags are replaced as `__tags`.

So when you use dot operator you can see `__tags` in the list of functions.

```python
# 54_private_members.py
print(cloud.__tags)
```

While running the above code you will get an attribute error, because tagcloud object doesn't have this attribute.

There is a way to access this in a different way.
```python
# 54_private_members.py
cloud = TagCloud()
cloud.__dict__
```

Dictionary holds all the attributes in the class.
```python
# 54_private_members.py
print(cloud.__dict__)
```

If we print this instead of above:
```python
# 54_private_members.py
print(cloud._TagCloud__tags)
```

So, we get that from this chapter that in python there is no private members concept, these private members are still accessible from outside.

Using double underscores is more of a convention to prevent accidental access of these private members.


# Properties

There will be situations to control over an attribute in class with the implication below, you can create an object called Product

```python
# 55_properties.py
class Product:
    def __init__(self, price):
        self.price = price

product = Product(-50)
```

To ensure that there is no negative price for the Product, we can make this field private and then getting there are two methods for getting and setting the value of this attribute

```python
# 55_properties.py
def __init__(self, price):
    self._price = price

def get_price(self):
    return self._price

def set_price(self, value):
    if value < 0:
        raise ValueError("Price cannot be negative")
    self._price = value
```

Now going back to our `__init__` function, instead of directly setting the price attribute, you call `self.set_price` and call price as initial value.

```python
# 55_properties.py
def __init__(self, price):
    self.set_price(price)
```

The implication is unpythonic, then you can use a property.
A property is an object that sits in front of an attribute and allows to set or get the value of an attribute.

The property function takes four parameters:
1. A function for getting value of attribute.
2. A function for setting the value of attribute.
3. A function deleting attribute.
4. For documentation.

```python
# 55_properties.py
price = property(get_price, set_price)
```

The property object will use this function for getting the value of the price attribute.

⇒ Coming back to price of our product:
```python
# 55_properties.py
product = Product(10)
```

→ If you use dot operator on the product:
![syntax demo](/images/55_properties_screenshot.png)

⇒ Simply print product price
```python
# 55_properties.py
print(product.price)
```

⇒ we can also get set get_price and set_price as private

⇒ also we can use decorator to achieve the same result simpler and cleaner way.

Earlier we used a decorator called classmethod to convert an instance method and a class method.  
Another decorator for creating a property called property decorator.  
Instead of using property function you can use property decorator.

```python
# 55_properties.py
@property
def price(self):
    return self._price
```

```python
# 55_properties.py
@price.setter
def price(self, value):
    if value < 0:
        raise ValueError("price cannot be negative")
    self._price = value
```

These two decorators (@property and @price.setter) can easily create a property.

Also change:
```python
# 55_properties.py
class Product:
    def __init__(self, price):
        self.price = price
```


# Inheritance

While building classes, you may notice that some classes have one or more features or functions in common.

For example:

```python
# 56_inheritance.py
class Mammal:
    def eat(self):
        print("eat")

    def walk(self):
        print("walk")
```

Here mammals is considered as class and they should be able to eat and walk.

Another example is fish. They should be able to eat but fish don't walk, and they swim.

```python
# 56_inheritance.py
class Fish:
    def eat(self):
        print("eat")

    def swim(self):
        print("swim")
```

In both classes, we have duplicated the eat method.
In real world problems, we will need to repeat this method in various classes. In such situation, don't repeat yourself, we have two solutions - inheritance and composition.

In this chapter, we are going to study inheritance and composition is studied later in the section.

Inheritance is a mechanism that allows us to define the common behaviour or common functions in one class, and then inherit them in other classes.

Here is how it works:

```python
# 56_inheritance.py
class Animal:
    def eat(self):
        print("eat")

class Mammal(Animal):
    def walk(self):
        print("walk")
```

→ In the above situation we refer animal as Parent or Base class and mammals as child or sub class.

→ Same can be applied to fish class.

→ In these inheritance methods, you can also inherit the attribute of a base class.

```python
# 56_inheritance.py
m = Mammal()
m.eat()
```

```python
# 56_inheritance.py
class Animal:
    def __init__(self):
        self.age = 1
```

Now when we create mammal object, it will automatically have age attribute Initialized to 1.

```python
# 56_inheritance.py
print(m.age)
```


# The object Class

Here lets discuss a few couple of useful built-in functions.

→ "isinstance()" – To check if object is an instance of a given class

```python
# 57_the_object_class.py
m = Mammal()
isinstance(m, Mammal)
```

- This is to check if m is an instance of mammal.

```python
# 57_the_object_class.py
print(isinstance(m, Mammal))
```

- If we pass Animal instead of Mammal:
```python
# 57_the_object_class.py
print(isinstance(m, Animal))
```

→ This animal class is inherited from a class called object, and that is the base class for our classes in Python.

→ Every classes in Python is directly or indirectly derives from Object class.

→ Going back to instance of object let's see if m is an instance of object 
```python
# 57_the_object_class.py
print (isinstance(m, object)).
```

→ Run the program and the result will be true.

So we get that mammals inherits from animal, which inherits from object.

→ There is also a built-in-function for creating an empty object:
```python
# 57_the_object_class.py
o = object()
```

If you use dot operator on o, you can see all these magic methods:
These all are many magic methods that every class in Python has.
![syntax demo](/images/57_the_object_class.png)

→ If we use dot operator on m, you can see mammal class also has these methods. Because it is inherited from the base object.

→ Another built in function that you might find useful is "issubclass()"

→ With this you can see if a class derives from another class.

→ To see if mammal is a subclass of Animal:
```python
# 57_the_object_class.py
print(issubclass(Mammal, Animal))
```
Output will be true

→ If we change Animal to object we will get True because mammal indirectly inherits from the object class.


# Method Overriding

To add weight to mammal class similarly to age that we have added in Animal class in last example.

```python
# 58_method_overriding.py
class Animal:
    def __init__(self):
        self.age = 1
    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        self.weight = 2
    def walk(self):
        print("walk")

m = Mammal()
print(m.age)
print(m.weight)
```

⇒ when you run the above code, since mammal object has no attribute age, you will get error.

⇒ The reason for this error is because the constructor in animal class is not executed

⇒ Or in other words, the constructor in the mammal class replaced

When you redefine a method in the base class in the derived class, it's called method overriding or replacing a method in the base class.

To avoid this problem, we need to call the constructor of the base class. We use super() function to get access to the base class.

```python
# 58_method_overriding.py
class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1
    def eat(self):
        print("eat")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

m = Mammal()
print(m.age)
print(m.weight)
```

Also we can change the order by making few changes in the code:

```python
# 58_method_overriding.py
class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()
```

- Now in the result you can see that the constructor of mammal was called first and then the constructor of animal.

- Summarizing this section, Method overriding means replacing or extending a method defined in the base class.

- In the above implementation, init method in the animal class is extended.

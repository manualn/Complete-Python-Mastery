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


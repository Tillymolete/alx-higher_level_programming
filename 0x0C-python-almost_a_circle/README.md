This is a python Almost circle task.

0. If it's not tested it doesn't work
All your files, classes and methods must be unit tested and be PEP 8 validated.

1. Base class
Writes the first class Base:
a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

2. First Rectangle
Writes a the class Rectangle that inherits from Base:
In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter

3. Validate attributes
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)

4. Area first
Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

5. Display #0
Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.

6. __str__
Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

7. Display #1
Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

8. Update #0
Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute

9. Update #1
Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes

10. And now, the Square!
Writes  the class Square that inherits from Rectangle:


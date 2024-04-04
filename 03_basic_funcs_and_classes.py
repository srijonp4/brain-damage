# Funcs
def myFunc(n, m):
    return n * m


# Can modify objects but not reassign
# unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
            # will only modify val in the helper scope
        # val *= 2
        # this will modify val outside helper scope
        nonlocal val
        val *= 2

    helper()
    print(arr, val)


nums = [1, 2]
val = 3
double(nums, val)


## Classes


class MyClass:
    # constructor
    def __init__(self, nums) -> None:
        self.nums = nums  # creating a class member variable
        self.size = len(nums)

    def getLength(self) -> int:
        return self.size

    def getDoubleLength(self) -> int:
        return self.getLength() * 2


cl = MyClass([4,5])

print(cl.getLength())
print(cl.getDoubleLength())



# NOTE : all concepts

""" In Python, classes are a way to create new types. They allow you to define the behavior and structure of objects. Here's an overview of key concepts related to classes in Python: """

""" 1. Class Definition: To define a class, use the `class` keyword followed by the class name. For example:
 """
class MyClass:
    pass

""" 2. Attributes: Attributes are data stored inside a class or instance and represent the state or properties of the object. They can be class attributes (shared among all instances) or instance attributes (specific to each instance). You can define attributes in the class's `__init__` method: """

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

""" 3. **Methods**: Methods are functions defined inside a class and are used to define the behavior of an object. The first parameter of a method is always `self`, which refers to the instance of the class: """

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

""" 4. **Instance Creation**: To create an instance of a class, you call the class as if it were a function, passing any required arguments to the `__init__` method:
 """
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

""" 
5. **Inheritance**: Inheritance allows you to create a new class based on an existing class. The new class (subclass) can inherit attributes and methods from the existing class (superclass):
 """
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        return f"{self.name} is studying {subject}."
    
""" 
6. **Encapsulation**: Encapsulation is the concept of restricting access to certain parts of an object to prevent accidental modification. In Python, you can achieve encapsulation by using private attributes (prefixed with `__`):
 """
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
""" 
7. **Polymorphism**: Polymorphism allows objects of different classes to be treated as objects of a common superclass. This is often achieved through method overriding:
 """
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


""" Classes are fundamental to object-oriented programming (OOP) in Python and provide a powerful way to structure and organize your code. """
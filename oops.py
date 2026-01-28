'''

#  Object Oriented Programming (OOP)

## 1. What is OOP?

* Object Oriented Programming (OOP) is a programming approach based on objects.
* It models real-world entities using classes and objects.
* OOP combines data (attributes) and functions (behaviour) into a single unit.



## 2. Object

* An object is a real-world entity.
* It has:

  * State → data / attributes
  * Behaviour → functions / methods
* Examples:

  * Student, Employee, Car, Invoice

'''

# s1 = Student()
#object s1 of class Student.

'''

## 3. Class

* A class is a user-defined blueprint or prototype.
* It defines:

  * What attributes an object will have
  * What methods an object can perform
* Objects are created from a class.
* One class can create multiple objects.
'''

# class Student:    class → keyword to create a class; Student → class name
#     pass          empty class


'''


## 4. Object vs Class

* Class → Design / Blueprint
* Object → Instance of the class
* Example:

  * Class → Student
  * Objects → Student1, Student2, Student3


'''

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Manasvi")
print(s1.name)



class car:
    def start(self):
        print("engine started ")
c1=car()
c1.start()

'''
## 5. Procedural Oriented Approach

* Program is written as a series of steps.
* Logic is divided into functions.
* Data and functions are separate.
* Data is shared using arguments and return values.
* Suitable for small programs.

### Limitation:

* Less security
* Difficult to manage large programs
* No direct binding between data and function



## 6. Object Oriented Approach

* Program is designed using classes and objects.
* Data and methods are combined.
* Focuses on real-world modeling.
* Suitable for large and complex programs.

### Advantages:

* Code reusability
* Data security
* Easy maintenance
* Better structure



## 7. Attributes

* Attributes represent the data of an object.
* Each attribute has a value.

### Examples:

* Student → name, class, subjects, marks
* Employee → name, designation, department, salary
* Invoice → invoice number, customer, product, price, quantity
* Car → registration number, owner, brand, speed

➡️ Attribute = Data



## 8. Behaviour

* Behaviour represents the actions performed on data.
* Behaviour is implemented using methods.

### Examples:

* Calculate percentage of student marks
* Compute employee incentives
* Apply GST on invoice
* Measure car speed

➡️ Behaviour = Function / Method



## 9. Relationship between Attributes and Behaviour

* Attributes and behaviour co-exist.
* Behaviour works on attributes.
* They are defined together inside a class.



## 10. Key Features of OOP

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction



## 11. Encapsulation

* Wrapping data and methods into a single unit (class).
* Helps in data hiding and security.
* Prevents direct access to data.



## 12. Inheritance

* One class acquires properties of another class.
* Promotes code reusability.
* Represents parent–child relationship.



## 13. Polymorphism

* One method can perform different tasks.
* Same function name, different behaviour.
* Achieved using:

  * Method overriding
  * Operator overloading



## 14. Abstraction

* Hides internal implementation details.
* Shows only essential features to the user.
* Improves simplicity and security.



## 15. Python OOP Keywords (Must Remember)

* `class` → define class
* `object` → instance of class
* `__init__()` → constructor
* `self` → refers to current object
* `super()` → access parent class
* Access levels:

  * Public
  * Protected (`_variable`)
  * Private (`__variable`)





* OOP organizes programs using real-world concepts.
* Makes code reusable, secure, and easy to manage.
* Python supports OOP fully and efficiently.

'''
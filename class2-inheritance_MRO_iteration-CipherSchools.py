class Animal:

    # attribute and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)

# create an object of the subclass
labrador = Dog()

# access superclass attribute and method 
labrador.name = "Rohu"
labrador.eat()

# call subclass method 
labrador.display()



class Animal:

    # attributes and method of the parent class
    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        print("I like to eat bones")

# create an object of the subclass
labrador = Dog()

# call the eat() method on the labrador object
labrador.eat()











class Animal:

    name = ""
    
    def eat(self):
        print("I can eat")

# inherit from Animal
class Dog(Animal):
    
    # override eat() method
    def eat(self):
        
        # call the eat() method of the superclass using super()
        super().eat()
        
        print("I like to eat bones")

# create an object of the subclass
labrador = Dog()

labrador.eat()
































class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")
 
r = B()
r.rk()








class A:
    def rk(self):
        print(" In class A")
class B(A):
    def rk(self):
        print(" In class B")
class C(A):
    def rk(self):
        print("In class C")
 
# classes ordering
class D(B, C):
    pass
    
r = D()
r.rk()


# Old style class
class OldStyleClass:
    pass
 
# New style class
class NewStyleClass(object):
    pass





class A:
    pass
 
 
class B:
    pass
 
 
class C(A, B):
    pass
 
 
class D(B, A):
    pass
 
 
class E(C,D):
    pass









# Python program to show the order
# in which methods are resolved
 
class A:
    def rk(self):
        print(" In class A")
class B:
    def rk(self):
        print(" In class B")
 
# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")
 
r = C()
 
# it prints the lookup order
print(C.__mro__)
print(C.mro())























# define a list
my_list = [4, 7, 0]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  # prints 4

# get the second element of the iterator
print(next(iterator))  # prints 7

# get the third element of the iterator
print(next(iterator))  # prints 0



# create a list of integers
my_list = [1, 2, 3, 4, 5]

# create an iterator from the list
iterator = iter(my_list)

# iterate through the elements of the iterator
for element in iterator:

    # Print each element
    print(element)
    
    
    
    
    
    
    
    
    class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i)) # prints 1
print(next(i)) # prints 2
print(next(i)) # prints 4
print(next(i)) # prints 8
print(next(i)) # raises StopIteration exception








for i in PowTwo(3):
    print(i)
    
    
    
    
    
from itertools import count

# create an infinite iterator that starts at 1 and increments by 1 each time
infinite_iterator = count(1)

# print the first 5 elements of the infinite iterator
for i in range(5):
    print(next(infinite_iterator))







# define a list
my_list = [4, 7, 0]

for element in my_list:
    print(element)





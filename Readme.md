<!-- Today's Topic -->

1. Encapsulation

Encapsulation is the capsule that protect the data and variable from accidental modification, unauthorized access.

yes, we can just created a varibale just using 2 underscore before a variable name like self.__brand = "toyota". 

2. Abstraction

Abstraction is basically a common method created in the parent class. Every child class must implement that method in its own way.

3. Magic/Dunder method

- __init__(self): its a constructer, which auto run auto     when we create a object.

- __len__(self): its also run auto but only when we run len funtion. 

- __str__(self): self method return string when We print the class.

- __add__(self): its runs when we try to of 2 items, (make sure 1 item is already available in the class, coz __add__ can only take 1 new argument)



<!-- Challene Question -->
# Week 3 Final Challenge

## Library Management System

Create an abstract class:

- LibraryItem

### Private Variables

- __title
- __author

### Abstract Method

```python
display()
```

Every child class must implement it.

---

## Create three child classes

- Book
- Magazine
- Newspaper

Each class should implement `display()` differently.

Example:

Book:
```
Book: Python Crash Course
Author: Eric Matthes
```

Magazine:
```
Magazine: National Geographic
Author: National Geographic Team
```

Newspaper:
```
Newspaper: The Hindu
Author: Editorial Team
```

---

## Magic Methods

Implement:

### `__str__()`

Printing an object should show:

```
Book(Python Crash Course)
```

### `__len__()`

Return the length of the title.

Example:

```
len(book)
```

returns

```
20
```

### `__add__()`

If two books are added,

```python
book1 + book2
```

return

```
Total title length: 35
```

---

## Main Program

Create one object of each class.

Store them in a list.

Use one loop to:

- call `display()`
- print the object
- print its length

Finally,

add two books using `+`.

---

## Rules

✅ Use Abstraction

✅ Use Encapsulation

✅ Use Inheritance

✅ Use Polymorphism

✅ Use `__str__()`

✅ Use `__len__()`

✅ Use `__add__()`

❌ No `if`, `elif`, `match-case`

# During solve this question I realize that I dont know much about magic methods, so I'am going to learn them. and make sure during solve this questoins I dont use chatbots.


# Magic Method Challenge Set

## Challenge 1 - __init__()

Create a `Student` class.

- Store:
  - name
  - roll
  - course

Create 3 student objects and print their details.

---

## Challenge 2 - __str__()

Create a `Laptop` class.

When you write:

```python
print(laptop)
```

Output:

```
Laptop: Dell Inspiron
Price: ₹55000
```

---

## Challenge 3 - __len__()

Create a `Movie` class.

`len(movie)` should return the number of characters in the movie name.

Example:

```
Movie = "Interstellar"

len(movie)

Output:
12
```

---

## Challenge 4 - __add__()

Create an `Employee` class.

Store:

- name
- salary

If two employees are added:

```python
emp1 + emp2
```

Return:

```
Total Salary: 85000
```

---

I only know __init__, __add__, __len__, __str__. but there is lots more magic method so no i gonna learn them.

Comparison Methods
__eq__()        ==
__ne__()        !=
__lt__()        <
__le__()        <=
__gt__()        >
__ge__()        >=

Arithmetic Methods
__sub__()       -
__mul__()       *
__truediv__()   /
__floordiv__()  //
__mod__()       %
__pow__()       **

Membership
__contains__()   in

Indexing
__getitem__()    obj[index]
__setitem__()    obj[index] = value
__delitem__()    del obj[index]

Callable Object
__call__()

Iteration
__iter__()
__next__()

Boolean
__bool__()

Representation
__repr__()

Attribute Access
__getattr__()
__setattr__()
__delattr__()

I'll learn them in free time, not all together
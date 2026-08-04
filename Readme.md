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
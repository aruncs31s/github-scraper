---
tags:
  - project
  - electronics
title: Test Project
description: This is a test description 
---
# Full Adder "Change ME"
![alt text|600x500](imgs/main.png)
This section should contain the description and introduction to the project. 
## Code 

```python
"""
This script is here only for to give an example.
""" 

def f_adder(x,y,c_in):
    sum = int(
        (
            not x and y or 
            not y and x 
        ) 
        and
        not c_in  or not  
        (
            not x and y or
            not y and x 
        )
        and c_in) 
    carry = int(
        (
            not x and y or 
            not y and x 
        ) 
        and
        not c_in  or not  
        (
            not x and y or
            not y and x 
        )
        and c_in)
    return sum, carry
print("Truth Table of Full Adder".center(len("x | y | c_in | sum | carry |"), "-"))
print("-".center(len("x | y | c_in | sum | carry |"), "-"))
print("x | y | c_in | sum | carry |")
for x in [0, 1]:
    for y in [0, 1]:
        for c_in in [0, 1]:
            sum, carry = f_adder(x, y, c_in)
            print(f"{x} | {y} | {c_in} {" " * (len("c_in") - 2)} | {sum} {" " * (len("sum") - 2)} | {carry} {" " * (len("carry") - 2)} |")
print("-".center(len("x | y | c_in | sum | carry |"), "-"))
print("End of Truth Table".center(len("x | y | c_in | sum | carry |"), "-"))
```

```
-Truth Table of Full Adder--
----------------------------
x | y | c_in | sum | carry |
0 | 0 | 0    | 0   | 0     |
0 | 0 | 1    | 1   | 1     |
0 | 1 | 0    | 1   | 1     |
0 | 1 | 1    | 0   | 0     |
1 | 0 | 0    | 1   | 1     |
1 | 0 | 1    | 0   | 0     |
1 | 1 | 0    | 0   | 0     |
1 | 1 | 1    | 1   | 1     |
----------------------------
-----End of Truth Table-----
```



## Circuit Diagram 

![alt text](imgs/ckt_diagram.png)

Texts explaining the circuit diagram 
example explenation

This section contains the circuit diagram of a full adder circuit. It is made using BJT(BiPolar Junction Transistor).

### Working
There are 3 inputs and 2 outputs , 

## Simulations

![alt text](imgs/simulation_1.png)

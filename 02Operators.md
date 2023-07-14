# Operators

## Boolean

A boolean data type represents one of the two values: _True of False_. The use of these data types will be clear once we start using the comparison operator. The first letter "T" for True and "F" for False **Should be capital** unlike JavaScript.

## Assignment Operators

Assignment operators are used to assign values to variables.

![assignment_operators](./Images/assignment_operators.png)

## Arithmetic Operators

![arithmetic_operators](./Images/arithmetic_operators.png)

Example

```Python
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
```

## Comparison Operators

In programming we compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value.

![comparison_operators](./Images/comparison_operators.png)

In addition to the above comparison operator Python uses:

- _is_: Returns true if both variables are the same object (x is y).
- _is not_: Returns true if both variables are not the same object (x is not y).
- _in_: Returns True if the queried list contains a certain item (x in y).
- _not in_: Returns True if the queried list doesn't have a certain item (x not in y).

```Python
print(f'1 is 1: {1 is 1}')                   #True -> Because the data values are the same
print(f'1 is not 2: {1 is not 2}')           #True -> Because 1 is not 2
print(f'A in Asabeneh: {'A' in 'Asabeneh'}') #True -> A found in the string
print(f'B is Asabeneh: {'B' in 'Asabeneh'}') #False -> there is no uppercase B
print(f'coding {in} coding for all')         #True -> Because coding for all has the word 'coding'
print(f'a in an: {'a' in 'an'}')             #True
print(f'4 is 2 ** 2: {4 is 2**2}')           #True
```

## Logical Operators

Unlike other programming languages python uses keywords _and, or_ and _not_ for logical operators. Logical operators are used to combine conditional statements:

![logical_operators](./Images/logical_operators.png)

```Python
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
```

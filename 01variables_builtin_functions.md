# Introduction

Python is a high-level programming language for general porpose programming. It is an opensource, interpreted, objected-oriented programming language. Pythonwas created by a Dutch programmer, Guido van Rossum. The name of Python programming language was derived from a British sketch comedy series, _Month Python's Flying Circus_. The first version was released on February 20, 1991.

---

## - Varibles, Built-Functions -

### Built in functions

In python we have lots of built-in functions. Built-in functions are globally available for your use that mean you can make use of the built-in functions without importing or configuring. Some of the most commonly used Python built-in functions are the following:
_print(), len(), type(), int(), float(), str(), input(), list(), dict(), min(), max(), sum(), sorted(), open(), file(), help(), and dir()_.

- **print()** It prints the value in the console.

```python
  print('Hello world') #Hello world
  print(55 + 45) #100
```

- **len()** It counts the number of characters (including blank spaces).

```python
  len('Hello world') #11
  len('My car is red') #13
```

- **type()** It checks the data type

```python
  type('Hello world') # <class 'str'>
  type(73) # <class 'int'>
  type(72.8) # <class 'float'>
  type(True) # <class 'bool'>
  type([1, 2, 3, 4]) # <class 'list'>
```

- **str()** It converts number to string.

```python
  str(25) #'25'
```

- **int()** It converts string to number.

```python
  int('25') #25
```

- **float()** It converts integer or string to decimal.

```python
  float(25) #25.0
  float('72.9') #72.9
```

- **input()** It takes user input.

```python
  input("What's your name:") # What's your name: 'my_name'
```

- **help()** Prints all reserved word.

```python
  help(str) # Give information about string.
```

Here is a list of the python keywords. Enter any keyword to get more help.

![python_keywords](/Images/python%20keywords.png)

- **min()** Gives the minimum value

```python
  min(20, 30, 40, 50) # 20
  min([60, 45, 15, 65]) # 15 -> It takes list as an argument and return min value
```

- **max()** Gives the maximun value.

```python
  max(20, 30, 40, 50) # 50
  min([60, 45, 15, 65]) #65 -> It takes list as an argument and return max value
```

- **sum()** It takes only list as an argument and return the sum.

```python
  sum([60, 45, 15, 65]) # 185
```

---

### Variables

Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A Mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

#### Python variable name rules

- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-Z, 0-9, and \_).
- Variable names are case-sensitive. firstname, Firstname, FirstName and FIRSTNAME are different variables.

Valid variable names

```python
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2021
year2021
current_year_2021
birth_year
num1
num2
```

Invalid variable names

```python
first-name
first@name
first$name
num-1
1num
```

We will use standard Python variable naming style which has been adopted by many Python developes. Python developers use snake case (first_name, last_name, birth_year, etc) variable naming convention. We use underscore character after each word for a variable containing more than one word (first_name, last_name, birth_year, etc). The example below is an example of standard naming of variables, underscore is required when the variable name is more than one word.

Examples

```python
# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
```

Let's print and also find the length of the variables declared at the top:

Example:

```Python
# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name)) # 8 -> Asabeneh
print('Last name: ', last_name)
print('Last name length: ', len(last_name)) # 7 -> Yetayeh
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
```

### Data Types

There are several data types in Python. To identify the data type we use the _type_ built-in function. I would like to ask you to focus on understanding different data types ver well. When it comes to programming, it is all about data types.

### Numbers

Number data types in Python:

1. **Integers:** Negatives, zero, positives -> -3, -2, -1, 0, 1, 2, 3...
2. **Floating Point Numbers:** Decimal numbers -> -3.5, -22.45, 25.4, 1000.32...
3. **Complex Numbers:** -> 1 + 1j, 2 + 4j, 1 - 1j...

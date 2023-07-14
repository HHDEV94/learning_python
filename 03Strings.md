# Strings

Text is a string data type. Any data type written as text is a string. Any data under single, double or triple quote are strings. There are different string methods and built-in functions to deal with string data types. To check the length of a string use the len() method.

## Creating a String

```Python
letter = 'P'                  #A string could be a single character or a bunch of texts
print(letter)                 #P
print(len(letter))            #1

greeting = 'Hello, everyone'  #String could be made using a single or double quote, "Hello, everyone"
print(greeting)               #Hello, everyone
print(len(greeting))          #15

sentence = 'I am learning Python :)'
print(sentence)
```

Multiline string is created by using triple single(''') or triple double quotes(""").
Example:

```Python
multiline_string = '''I am a student and enjoy learn.
I want to be the best and create many programs in Python.
This is a multiline text.'''
print(multiline_string)

#Another way of doing the same thing
multiline_string = """I am a student and enjoy learn.
I want to be the best and create many programs in Python.
This is a multiline text."""
print(multiline_string)
```

## String concatenation

We can connect strings together. Merging or connecting strings is called concatenation.
Example:

```Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name

print(full_name) #Asabeneh Yetayeh
```

## Escape sequences in strings

In Python and other programming languages \ followed by a character is an escape sequence. Let's see the most common escape characters:

- \n -> new line
- \t -> Tab means (8 spaces)
- \\\ -> Back slash
- \\' -> Single quote (')
- \\" -> Double quote (")

```Python
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# output
# I hope every one is enjoying the Python Challenge.
# Are you ?
# Days  Topics  Exercises
# Day 1   5      5
# Day 2   6      20
# Day 3  5      23
# Day 4   1      35
# This is a backslash  symbol (\)
# In every programming language it starts with "Hello, World!"
```

## String formatting (str.format)

```Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# output
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

```

## String interpolation / f-strings

Another formatting way is string interpolation, f-strings. Strings start with 'f' and we can inject the data in their corresponding positions.

```Python
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
```

## Python strings as sequence of characters

Python strings are sequences of characters, and share their basic methods of access with other Python ordered sequences of objects - list and tuples. The simplest way of extracting single characers from strings (and individual members from any sequence) is to unpack them into corresponding variables.

Unpacking Characters

```Python
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```

## Accessing characters in strings by index

In programming counting starts from zero. Therefore the first letter of a string is at zero index and the last letter of a string si the length of a string minus one.

```Python
language = 'Python'
first_letter = language[0]
print(first_letter) # P

second_letter = language[1]
print(second_letter) # y

last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
```

If we want to start from right end we can use negative indexing. -1 is the last index.

```Python
language = 'Python'
last_letter = language[-1]
print(last_letter) # n

second_last = language[-2]
print(second_last) # o
```

## Slicing Python strings

In python we can slice strings into strings into substrings.

```Python
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) # Pyt

last_three = language[3:6]
print(last_three) # hon
last_three = language[3:]
print(last_three) # hon
```

## reversing a string

We can easily reverse strings in python.

```Python
greeting = 'Hello, everyone'
print(greeting[::-1]) #enoyreve ,olleH
```

## String Methods

There are many strings methods which allow us to format strings. See some of the string methods in the following example:

- **catipalize():** Converts the first character of the string to capital letter

```Python
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
```

- **count():** Returns occurrences of substring in string, count(substring, start=..., end=..). The start is a starting indexing for counting and end is the last index to count.

```Python
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1,
print(challenge.count('th')) # 2`
```

- **endswith():** Checks if a string ends with a specified ending.

```Python
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
```

- **expandtabs():** Replaces tab charactyer with spaces, default tab size is 8. It takes tab size argument.

```Python
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
```

- **find():** Returns the index of the first occurrence of a substring, if not found retunrs -1.

```Python
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 1
```

- **rfind():** Returns the index of the last occurrence of a substring, if not found returns -1.

```Python
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17
```

- **index():** Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length -1). If the substring is not found it raises a valueError.

```Python
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error
```

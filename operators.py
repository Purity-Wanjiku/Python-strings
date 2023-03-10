>>> x = "Go home"
>>> len (x)
7
>>> "o" in x
True
>>> "p" in x
False
>>> s.upper(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 's' is not defined
>>> s.upper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 's' is not defined
>>> x.upper()
'GO HOME'
>>> x.lower()
'go home'
>>> x.title()
'Go Home'
>>> x.capitalize()
'Go home'
>>> x.lower()
'go home'
>>> x.capitalize()
'Go home'
>>> y="I want to call home"
>>> y.title()
'I Want To Call Home'
>>> y.lower()
'i want to call home'
>>> y.capitalize()
'I want to call home'
>>> y.count()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: count() takes at least 1 argument (0 given)
>>> y.count("a")
2
>>> y.replace("a","x")
'I wxnt to cxll home'
>>> is.alpha()
  File "<stdin>", line 1
    is.alpha()
    ^
SyntaxError: invalid syntax
>>> dir(y)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> y.endswith("j")
False
>>> y.endswith("e")
True
>>> y.isalpha()
False
>>> x.isalpha()
False
>>> x.capitalize()
'Go home'
>>> x.upper()
'GO HOME'
>>> x.isalpha()
False
>>> print(x)
Go home
>>> x.isalnum()
False
>>> x.isdigit()
False
>>> x.lower()
'go home'
>>> x.isalpha()
False
>>> x.isalnum()
False
>>> x="banana"
>>> x.isalpha()
True
>>> x.isalnum()
True
>>> x.islower()
True
>>> x.isupper()
False
>>> x.isnumeric()
False
>>> x.index("n")
2
>>> x.index("b")
0
>>> y
'I want to call home'
>>> y
'I want to call home'
>>> y.index("e")
18

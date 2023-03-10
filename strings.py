                 ^
SyntaxError: unmatched ')'
>>> s=("AkiraChix")
>>> s[1]
'k'
>>> s[0]
'A'
>>> s[2]
'i'
>>> s[3]
'r'
>>> s[4]
'a'
>>> s[5]
'C'
>>> s[6]
'h'
>>> s[9]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> s[8]
'x'
>>> s[-8]
'k'
>>> s[-1]
'x'
>>> s
'AkiraChix'
>>> s[-1]
'x'
>>> s[-10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> s[-0]
'A'
>>> s[-1]
'x'
>>> s[-2]
'i'
>>> s[-3]
'h'
>>> s[-4]
'C'
>>> s[-5]
'a'
>>> s[-6]
'r'
>>> s[-7]
'i'
>>> s[-8]
'k'
>>> s[-9]
'A'
>>> s[i:4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'i' is not defined
>>> s["i":4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: slice indices must be integers or None or have an __index__ method
>>> s[1:4]
'kir'
>>> s[0:3]
'Aki'
>>> s[4:8]
'aChi'
>>> s[3: ]
'raChix'
>>> s[ :6]
'AkiraC'
>>> s
'AkiraChix'
>>> s[ :-6]
'Aki'
>>> s[-5:-2]
'aCh'
>>> s[-8:-6]
'ki'
>>> s[-4: ]
'Chix'
>>> s[-5:8]
'aChi'
>>> s[-6:7]
'raCh'
>>> s[1:-3]
'kiraC'
>>> s[3:-3]
'raC'
>>> s[-3:3]
''
>>> x = [1,2,5,8]
>>> x
[1, 2, 5, 8]
>>> y = "b2
  File "<stdin>", line 1
    y = "b2
          ^
SyntaxError: EOL while scanning string literal
>>> y = ["b."a","ewe","True,"False"] 
  File "<stdin>", line 1
    y = ["b."a","ewe","True,"False"] 
             ^
SyntaxError: invalid syntax
>>> y = ["b","a","ewe","True,"False"] 
  File "<stdin>", line 1
    y = ["b","a","ewe","True,"False"] 
                              ^
SyntaxError: invalid syntax
>>> y = ["b","a","ewe","True,"False", 1,2,3,] 
  File "<stdin>", line 1
    y = ["b","a","ewe","True,"False", 1,2,3,] 
                              ^
SyntaxError: invalid syntax
>>> type z
  File "<stdin>", line 1
    type z
         ^
SyntaxError: invalid syntax
>>> type (z)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'z' is not defined
>>> y = ["b","a","ewe",True,False, 1,2,3,] 
>>> last "list"
  File "<stdin>", line 1
    last "list"
         ^
SyntaxError: invalid syntax
>>> last "list">
  File "<stdin>", line 1
    last "list">
         ^
SyntaxError: invalid syntax
>>> b = [1,2,3,3,}
  File "<stdin>", line 1
    b = [1,2,3,3,}
                 ^
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> b = [1,2,3,3,]
>>> d=a*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> a= [1,2,3,4]
>>> c = a+b
>>> print(c)
[1, 2, 3, 4, 1, 2, 3, 3]
>>> type (y)
<class 'list'>
>>> dir (y)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> fruits = ["mango","apple","banana","passion","melon"]
>>> fruit apend("pineaple")
  File "<stdin>", line 1
    fruit apend("pineaple")
          ^
SyntaxError: invalid syntax
>>> fruits append("pineaple")
  File "<stdin>", line 1
    fruits append("pineaple")
           ^
SyntaxError: invalid syntax
>>> fruits append["pineaple"]
  File "<stdin>", line 1
    fruits append["pineaple"]
           ^
SyntaxError: invalid syntax
>>> fruits.append["pineaple"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> fruits.append ("pineaple")
>>> fruits
['mango', 'apple', 'banana', 'passion', 'melon', 'pineaple']
>>> fruits.extend(["orange","grapes"]
... fruits
  File "<stdin>", line 2
    fruits
    ^
SyntaxError: invalid syntax
>>> fruits.extend(["orange","grapes"])
>>> fruits
['mango', 'apple', 'banana', 'passion', 'melon', 'pineaple', 'orange', 'grapes']
>>> fruits.insert(" ","avocado")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> fruits.insert(" ,"avocado")
  File "<stdin>", line 1
    fruits.insert(" ,"avocado")
                      ^
SyntaxError: invalid syntax
>>> fruits.insert(1 ,"avocado")
>>> fruits
['mango', 'avocado', 'apple', 'banana', 'passion', 'melon', 'pineaple', 'orange', 'grapes']
>>> fruits.sort()
>>> fruits
['apple', 'avocado', 'banana', 'grapes', 'mango', 'melon', 'orange', 'passion', 'pineaple']
>>> fruits.reverse()
>>> fruits
['pineaple', 'passion', 'orange', 'melon', 'mango', 'grapes', 'banana', 'avocado', 'apple']
>>> fruits.remove("melon")
>>> fruits
['pineaple', 'passion', 'orange', 'mango', 'grapes', 'banana', 'avocado', 'apple']
>>> fruits.pop()
'apple'
>>> fruits
['pineaple', 'passion', 'orange', 'mango', 'grapes', 'banana', 'avocado']
>>> fruits.pop()
'avocado'
>>> fruits
['pineaple', 'passion', 'orange', 'mango', 'grapes', 'banana']
>>> len (fruits)
6
>>> fruits = ("mango","Banana","passion")
>>> fruits[0]
'mango'
>>> fruits[0]
'mango'
>>> fruits[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> fruits[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> fruits
('mango', 'Banana', 'passion')
>>> fruits[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> fuits[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fuits' is not defined
>>> fruits[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> fruits[3:4]
()
>>> fruits[3:4]
()
>>> fruits
('mango', 'Banana', 'passion')
>>> fruits[1]
'Banana'
>>> fruits[2]
'passion'
>>> fruits[ :2]
('mango', 'Banana')
>>> x = [1,2,3,4,5]
>>> x
[1, 2, 3, 4, 5]
>>> for n in x.print(n)
  File "<stdin>", line 1
    for n in x.print(n)
                      ^
SyntaxError: invalid syntax
>>> for n in x:print(n)
... 
1
2
3
4
5
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for n in x:print(n)
... 
1
2
3
4
5
>>> for n in x:print(n*10)
... 
10
20
30
40
50
>>> for n in x:print(n^2)
... 
3
0
1
6
7
>>> for n in x:print(n*n)
... 
1
4
9
16
25
>>> fruit.upper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fruit' is not defined
>>> fruits
('mango', 'Banana', 'passion')
>>> fruits.upper()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'upper'
>>> for n in x:print(n.upper())
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'upper'
>>> for n in x:print(n.upper))
  File "<stdin>", line 1
    for n in x:print(n.upper))
                             ^
SyntaxError: unmatched ')'
>>> for n in x:print(fruits.upper))
  File "<stdin>", line 1
    for n in x:print(fruits.upper))
                                  ^
SyntaxError: unmatched ')'
>>> for n in x:print(fruits.upper())
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'upper'
>>> for f in fruits:print(x.upper())
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'upper'
>>> for f in fruits:print(f.upper())
... 
MANGO
BANANA
PASSION
>>> for fruit in fruits:print(f.lower())
... 
passion
passion
passion
>>> for f in fruits:print(f.lower())
... 
mango
banana
passion
>>> 

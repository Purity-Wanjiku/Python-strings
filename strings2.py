>>> a = "The best things in life are free!"
>>> print("expensive" not in a)
True
>>> print("free" in a)
True
>>> if "free" in a:print("Yes, `free` is present.")
... 
Yes, `free` is present.
>>> print(len(a))
33
>>> for x in "banana": print(x)
... 
b
a
n
a
n
a
>>> print(a[3])
 
>>> print(a[4])
b
>>> a[2]
'e'
>>> a[-2]
'e'
>>> print(a)
The best things in life are free!
>>> a[-0]
'T'
>>> a[-1]
'!'
>>> a[-2]
'e'
>>> a[-3]
'e'
>>> a[-4]
'r'
>>> a[-5]
'f'
>>> a[-6]
' '
>>> a[-7]
'e'
>>> a[-8]
'r'
>>> a[-9]
'a'
>>> a[-10]
' '
>>> a[-11]
'e'
>>> a[-12]
'f'
>>> a[-13]
'i'
>>> a[-14]
'l'
>>> a[-15]
' '
>>> a[-16]
'n'
>>> a[-17]
'i'
>>> a = "Eat this!"
>>> a[-0]
'E'
>>> a[-1]
'!'
>>> a[-2]
's'
>>> a[-3]
'i'
>>> a[-4]
'h'
>>> a[-5]
't'
>>> a[-6]
' '
>>> a[-7]
't'
>>> a[-8]
'a'
>>> a[-9]
'E'
>>> a[-10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> #You can return a range of characters by using the slice syntax.
>>> a[2:5]
't t'
>>> #character in position 5 is not included/printed
>>> a[1:3]
'at'
>>> a[1:4]
'at '
>>> a[1:]
'at this!'
>>> #Get the characters from position 1, and all the way to the end
>>> a[-1:]
'!'
>>> a[:-1]
'Eat this'
>>> a[-3:]
'is!'
>>> a[-1:-4]
''
>>> a[-2:-6]
''
>>> print(a)
Eat this!
>>> a[-6:-2]
' thi'
>>> #gets the character "i" from position -6 to, but not included:"s" in position-2
>>> a[-3:]
'is!'
>>> #gets the character "i" from position -3 till the end

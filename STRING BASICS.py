# we can also assign a multiple line string
x='''oranges 
are
orange in 
colour
'''
print(x)
# string in python is basically array
x= "hello, World!    "
print(x)
print(x[11])
# we can also print the letters of string; e.g :-
for a in x:
    print(a)
# we can also print the length of the string
print(len(x))
# we can also check the certain  value inside the string
y="hello,from the world"
print("the"in y)
print("like"in y)
print(x[2:5])
print(x[6:13])
print(x[:5])
print(x[4:])
print(x[-5:-2])
print(x.upper())
print(x.lower())
# we can also remove right spaces by help of strip() syntax
print(x.strip())
# we can also replace a letter or word from the string by another letter or word
print(x.replace("h","y"))
print(x.split(','))
# concatenation ie it adds two words/letters
a='HELLO'
b='WORLD'
print(a+b)
#to get spaces b/w hello and world
print(a+"  "+b)

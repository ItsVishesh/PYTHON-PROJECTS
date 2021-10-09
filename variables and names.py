#                  variable
# variable :- variable is used to store data value
# for ex :- x=5


x=5
y="john"
print(x)
print(y)

x=5
x="john"
print(x)

x=str(5)
y=int(5)
z=float(5)

print(x)
print(y)
print(z)
# type() is used to know the type of data value
print(type(x))
print(type(y))
print(type(z))
# we can declare string in single or double inverted commas;
a="john"
b='john'
print(a)
print(b)
#                        variable name
# There is a different value for small a and capital A
a=6
A=4
print(a)
print(A)

#variables can contain letters(a to z) ,numbers(0 to 9)  and underscores(_);
adf12=5
print(adf12)

ar_=20
print(ar_)

fg_12=89
print(fg_12)

# but we cannot start the variable name with number,its shows us syntax error;
"""2sf=34
print(2sf)"""

# we can able to assign multiple varibles with multiple different values;
a= "apple"
b=" ball"
c="cat"
print(a)
print(b)
print(c)
# we can also assign above lines of code in single line;

x,y,z="bananas","cherry","oranges"
print(x)
print(y)
print(z)

# we can also assign multiple variables to one value
x=y=z= 'oranges'
print(y)

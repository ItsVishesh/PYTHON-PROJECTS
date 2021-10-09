a="Hello World"
print(id(a))
b=a
print(b)
a=2
print(b)
print(a)

c=10
print(id(c))
d=c
print(id(d))
c=20
print(id(c))
print(id(d))
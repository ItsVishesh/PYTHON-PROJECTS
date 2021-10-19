colour = ["blue","pink","red","orange","yellow",17]
#print(colour)
#print(colour[0])
#print(colour[1])
#print(colour[2])
#print(colour[3])
#print(colour[4])
#print(colour[5])

numbers = [2,7,15,3,10]
#numbers.sort() # sorts the list
#numbers.reverse() # reverses the order of  the list
#print(numbers)
#print(numbers[4])
#print(numbers[:])
#print(numbers[:5])
#print(numbers[0:5])
#print(numbers[1:])
#print(numbers[1:4])
#print(numbers[::])
#print(numbers[::2])
#print(numbers[::3])
#print(numbers[::-1])
#print(numbers[::-2])
#print(numbers[1:4:-1])
#print(len(numbers))
#print(min(numbers))
#print(max(numbers))
#print(numbers[-5:-1])
#print(numbers[-5:-1:2])
#print(numbers[-5:-2])
#print(numbers[-5:1:2])
#print(numbers[-5:4:1])
#print(numbers[-4:3:1])
#print(numbers[0:-4])
#print(numbers[2:-2])
#numbers.append(8)  # add an element at the end of the list
#numbers.append(45)
#numbers.append(3)
#numbers.sort()
#print(numbers)
'''numbers2 = []
numbers2.append(2)
numbers2.append(67)
numbers2.append(34)
print(numbers2)'''
# insert() : - adds an element at the specified position
#numbers.insert(1,9) # yha pr 1 index value hai aur 9 vo value hai jisse hume insert karna hai. to humari 9 value ,index 1 pe insert hojayegi..
#numbers.insert(2,78) # ase hi 78 index value 2 pe insert hogi..
#print(numbers)
#numbers.remove(15) # it removes the element you want to remove.It takes an argument
# pop() :- removes the element at the specified position
#numbers.pop() # it removes last element
#numbers.pop(4) # it removes value present at index 4
#print(numbers)
'''numbers[1] = 67 # list ki value change ho sakti hai i.e list is mutable
print(numbers)'''
""" Mutable - can change
Immutable - cannot change
"""
#tupple = (1,2,3)
#tupple[1] = 8 # tupple ki value change nhi hoti i.e it is immutable
#tupple =(1) # yha humara brackets nhi ayenge mtlb tupple nhi bnega
# uske liye hume extra comma dena hoga
'''tupple = (1,) # ab tupple ban jayega
print(tupple)'''
'''a=1
b=8           # swapping of two numbers
a,b = b,a
print(b)'''
'''numbers.clear() # removes all the elements from the list
print(numbers)
'''
'''x=numbers.count(7)   # returns the number of elements with the specified value
print(x)
'''
'''x = numbers.copy() # returns a copy of the list
print(x)'''
'''x=numbers.index(3) # returns the positon at the first occurrence of the specified value.what is the position of the 3
print(x)'''
'''cars = ['ford','bmw','volvo']
numbers.extend(cars)  # it adds the elements of the any iterable(list or tupple or set),to the end of the current list
print(numbers)'''



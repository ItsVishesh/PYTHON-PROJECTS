# To insert characters that are illegal in a string,use an escape character.
# An escape characters is a backslah \ followed by the character you want to insert.
# An ex of an illegal character is a double qoute inside a string that is surrounded by double qoutes.
# ex :-
"""txt="we are the so-called "vikings" from the north."
print(txt)"""
# To fix the problem ,we use escape character \":
# ex:- RESULT :- DOUBLE QUOTES , CODE :- \"
txt1 = "we are the so-called \"vikings\" from the north."
print(txt1)

# Others escape character used in python are:

# 1) RESULT :- Single Quote , CODE:- \'
txt2='It\'s alright'
print(txt2)

# 2) RESULT :- BACKSLASH , CODE :- \\
txt3 = "This will insert one \\ (backslash)."
print(txt3)

# 3) RESULT :- NEW LINE , CODE :- \n
txt4 = "Hello\nWorld!"
print(txt4)

# 4) RESULT :- CARRIAGE RETURN means its print only the code after \r, CODE :- \r
txt5 = "HELLO\rWORLD!"
print(txt5)

# 5) RESULT :- TAB,its create spaces b\w the words  , CODE :- \t
txt6 = "Hello\tWorld!"
print(txt6)

# 6) RESULT :- BACKSPACE,this erases one character ,CODE :- \b
txt7 = "Hello\bWorld!"
print(txt7)

# 7) A backslash followed by three integers will result in a octal value:
txt8 = "\110\145\154\154\157"
print(txt8)

# 8) A backslash followed by an 'x' and a hex number represents a hex value:
txt9 = "\x48\x65\x6c\x6c\x6f"
print(txt9)
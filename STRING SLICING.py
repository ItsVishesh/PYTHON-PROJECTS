mystr = "Vishesh is a good boy"
print(mystr)
# python me index 0 se start hoti hai. To V yha pr 0 hai...
print(mystr[6])
print(mystr[0:6]) # isme humara 0 included hai aur 6 excluded hai to isleye yha pr hum 6 ki jagah 7 lenge..
print(mystr[0:7])
print(len(mystr))
print(mystr[0:21])
print(mystr[0:34]) # jha tk string hai utni print kr dega
print(mystr[0:7:2]) # isse humara 1-1 character skip hoke ayega.YE last jo 2 value di hai usse hoga..
print(mystr[0:7:3]) # ye 2-2 character skip krega
print(mystr[0::2]) # ye humara puri string leke  1-1 character skip kr dega..
print(mystr[0:]) # ye puri string print krega
print(mystr[:7]) # yha pe ye 0 le lega aur 7 characters tk print kr dega

print(mystr[:]) # puri string print krega
print(mystr[::]) # puri string print krega
print(mystr[0:21:1]) # puri string print krega
print(mystr[:21:1]) # puri string print krega
print(mystr[::1]) # puri string print krega
print(mystr[::7]) #6-6 character skip krega
print(mystr[::56]) #isme 21 characters hai na ki 56 to isleye ye jha tk resolve kr payega utna dega mtlb sirf 1 character print krke dega
print(mystr[-3:])
print(mystr[-3:-2])
print(mystr[::-1])  # string ulti print krega
print(mystr[::-2]) # string ulti print krega with skipping of 1-1 character

 # STRING FUNCTION

print(mystr.isalnum()) # ye check krega string alpha + numeric hai ya nhi
print(mystr.isalpha()) # ye sirf check krega ki string alpha hai ya nhi
print(mystr.isascii())
print(mystr.isdigit())
print(mystr.isdecimal())
print(mystr.islower())
print(mystr.isupper())
print(mystr.isnumeric())
print(mystr.isspace())
print(mystr.isprintable())
print(mystr.isidentifier())
print(mystr.istitle())
print(mystr.endswith("boy"))
print(mystr.startswith("Vishesh"))
print(mystr.count("h"))
print(mystr.capitalize())
print(mystr.lower())
print(mystr.find(" j"))
print(mystr.upper())
print(mystr.replace("is","are"))
print(mystr.center(30,'*'))
print(mystr.title())
print(mystr.zfill(30))
print(mystr.swapcase())
print(mystr.strip('Vi'))
print(mystr.strip('y'))
print(mystr.split())
txt = "thank you for the music\n welcome to the jungle"
print(txt.splitlines())
print(txt.splitlines(True))
print(mystr.join('&&'
                 ''))
print(mystr.casefold())
print(mystr.index('o'))

for a in mystr:
    print(a)

print(mystr[-21:15:-1])
# hum string ki koi bhi index value ki value change nhi kr sakte isleye string humare immutables hote hai
''' mystr[3] = "j"
print(mystr) '''


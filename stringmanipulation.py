#word = "!!!HelloWorld!!!"
# print(len(word))
# print(word.find("e"))
# print(word.count('l'))
# s = "count,number of spaces"
# print(s.count(''))
# 
# print(word.isalpha())
# print(word.isdigit())
# print(word.isalnum())
# print(word.isupper())
# print(word.islower())
# print(word.istitle())
# print(word.endswith('d'))
# print(word.startswith('H'))
# print(word.upper())
# print(word.lower())
# print(word.title())
# print(word.capitalize())
# print(word.swapcase())

# print(word.strip('!'))
# print(word.lstrip('!'))
# print(word.rstrip('!'))
# title = 'How to search substrings of Python strings'  
# print(title.find('string'))  
# print(title.rfind('string'))  
# print(title.find('for'))  

# text = "apple-banana-orange-grape"  
# fruits = text.split('-', maxsplit=2)  
# print(fruits)  
# import itertools
# text = "Hello Guys"
# print(''.join(itertools.islice(text,0,6)))


text = "hello guys this is isha"
# replaced_text = text.replace(' ','@')
# print(replaced_text)
# print(text.find('Hello'))
# t = text.find('Hello')
# print(t)
# print(text.capitalize())
# print(text.title())
# b = text.title
# print(b)
# b = "Hello Guys"
# print(text.upper())

#using list comprehension
d = text.split(" ")
print(d)

# print("The original string is : " + str(text))
# res = [.upper() if not idx % 2 else ele.lower()
#        for idx, ele in enumerate(text)]

# res = " ".join(res)
# print("The alternate case string is : " + str(res))

# for a in range(len(d)):
#     if (a % 2 == 0):
#         d[a] = d[a].upper()
# print(d)

newlist = [ d[a].upper() if  (a % 2) == 0 else  d[a] for a in range(len(d))  ]
print(newlist)
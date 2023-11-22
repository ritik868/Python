str = "  Hello world!    "
str1 = "helloworld" 



print("String =", str)
print("lspace =",str.lstrip())
print("rspace =",str.rstrip())
print("Swapcase =",str.swapcase())
print("Endswith with ! =",str1.endswith(""))
print("Endswith with hello =",str.endswith("hello"))

print("Str1:", str1)
print("Capitalize =",str1.capitalize())
print("String to upper case =",str.upper())
print("Casefold (string to lower case) =",str.casefold())
print("Count of 'o' in string =",str.count('o'))
print("Find of 'o' in string=",str.find('o'))
print("Find of 'y' in string=",str.find('y'))
print("Index of 'l' in string=",str1.index('l'))
print("String is alphabet=",str1.isalpha())
print("String is digit=",str1.isdigit())
print("String is alpha-numeric=",str1.isalnum())

print("")
txt = "I love adventure trips with friends"
part = txt.partition("trips")
print("String: ",txt)
print("Partitioned string: ",part)

print("")
txt = "I love adventure trips with friends"
rep = txt.replace("adventure", "mountain")
print("Original string: ",txt)
print("Replaced string: ",rep)

print("")
txt = "I, love, adventure, trips, with, friends"
txt2 = "I# love# adventure# trips# with# friends"
txt2 = "I@ love@ adventure@ trips@ with@ friends"
split = txt.split(", ")
split2 = txt2.split("# ")
split3 = txt2.split("@", 2)
print("String: ",txt)
print("String: ",txt2)
print("Splitted string using ',': ",split)
print("Splitted string '#': ",split2)
print("Splitted string using max-split: ",split3)




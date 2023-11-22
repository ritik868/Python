str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

print("Choose the operation: ")
print("Concatination --> 1")
print("Length --> 2")
print("Compare Equality --> 3")

opr1 = input()
opr = int(opr1)

if (opr==1):
    print(str1 + str2)
    
elif (opr==2):
    print(f"Length of String 1: {len(str1)}")
    print(f"Length of String 2: {len(str2)}")
    
elif (opr==3):
    if (str1 == str2):
        print("String 1 and string 2 are equal")
    else:
        print("String 1 and string 2 are not equal")
else:
    print("Choose valid operation")
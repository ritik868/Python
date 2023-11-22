num = int(input("Enter the number to check whether it is Armstrong number :"))
length=len(str(num))
sum = 0
temp = num
# temp2 = int(temp)

while temp > 0:
    digit = temp%10
    temp //= 10 
    sum += digit**length

if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
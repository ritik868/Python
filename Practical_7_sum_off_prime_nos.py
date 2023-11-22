start = int(input("Enter start of range : "))
end = int(input("Enter end of range : "))
sum = 0
for num in range(start, end+1):
   for i in range(2, num):
     if(num%i == 0):
       break
     else:
        sum += num
print(f"Sum of prime numbers in the given range is {sum}")
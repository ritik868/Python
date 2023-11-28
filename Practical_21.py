import operator

# Define the dictionary
month_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31 }

# Ask the user for a month
m_name = input("Enter the name of the month: ").casefold().capitalize()

# Check if the input is a valid month
if m_name in month_days:
    print(f"The month of {m_name} has {month_days[m_name]} days.")
else:
    print("\nInvalid input.")
    
print("\n")

# Print all keys in alphabetical order
print("All keys in alphabetical order:")
print(sorted(month_days.items()))

print("\n")

#Print months with 31 days
print("Months with 31 days:")
for x in month_days:
    if(month_days[x] == 31):
        print(x , month_days[x])

print("\n")

sortedlist = sorted(month_days.items(),key = operator.itemgetter(1))
print (sortedlist)

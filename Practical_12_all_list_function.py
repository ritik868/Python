list1 = [1, 2, 3,"Hritik", ["Kartik", "Praful"]]
list2 = [1, 2, 3, 4, 5]
list3 = [1, 2, 3, 4, 5]
list4 = [2, 7, 4, 5, 3, 7]



#       #Slicing
# print(f"Size of list1 is: {len(list1)}")

# print(list1[ : ])
# print(list1[0 : 3])
# print(list1[0 : 5 : 2])
# print(list1[-1 : -5 : -1]) 
# print(list1[-1 : -5 : -2])
# print(list1[0 : 2] + [ list1[4][0] ])

#      #<---Concatination--->
# print(list2)
# print(list3)
# concatinated_list = list2 + list3
# print(concatinated_list)

    #<--Extend-->
# list2.extend(list3)
# print(list2)

     #<--Append-->
# list2.append(list3)
# print(list2)

#<--Identity operator-->
# list4 = [1, 2, 3, 4, 5]
# list5 = [1, 2, 3, 4, 5]
# list6 = list4

# print(list4 is list5)
# print(list4 is list6)

# print(list4 is not list5)
# print(list4 is not list6)



#<--Membership operator-->
# print(f"Element in list2: {list2}")
# print(f"Is 3 present in list2: {3 in list2}")
# print(f"Is 5 not present in list2: {3 not in list2}")

#<--Use of min and max Function-->
# print(list2)
# print(f"Largest element: {max(list2)}")
# print(f"Smallest element: {min(list2)}")


# #<--List to string-->
# list_string = ['Deepak', "Hritik", "Kartik", "Praful"]
# print("List : ", list_string)
# print(f"List to string: ", ", ".join(list_string))

#  #<--Using membership operator-->
# list_string2 = ' '
# for x in list2:
#     list_string2 += str(x) + ', '

# print(f"List 2 : {list2}")
# print(f"List 2 to string : {list_string2}")


# #<--Comparison of lists-->
# print(f"List 2 : {list2}")
# print(f"List 3 : {list3}")

# if (list2 == list3):
#     print("List2 and List3 are equal")
# else:
#     print("List2 and List3 are not equal")
    
    
# print(f"List 2 : {list3}")
# print(f"List 3 : {list4}")

# if (list3 == list4):
#     print("List3 and List4 are equal")
# else:
#     print("List3 and List4 are not equal")

# print(f"List: {list2}")
# print(f"Sum of list: {sum(list2)}")

# print(f"List: {list4}")
# appended_list = list4.append(10)
# print(f"Append 10 to list: {list4}")


# print(f"List: {list4}")
# appended_list = list4.clear()
# print(f"List 4 (cleared) : {list4}")


# print(f"List: {list4}")
# print(f"Count of 7 : {list4.count(7)}")


# print(f"List: {list4}")
# print(f"Index of 7 : {list4.index(7)}")


# print(f"List: {list4}")
# list4.remove(7)
# print(f"new list after removal of 7 : {list4}")


# print(f"List: {list4}")
# list4.pop()
# print(f"pop : {list4}")

# print(f"List: {list4}")
# list4.pop(2)
# print(f"pop at index 2: {list4}")


# print(f"List1: {list4}")
# list5 = ['Boy', 'plays', 'cricket']
# print(f"List2: {list5}")
# list4.sort()
# list5.sort()
# print(f"List1 in ascending order: {list4}")
# print(f"List2 in ascending order: {list5}")

# list4.sort(reverse = True)
# list5.sort(reverse = True)
# print(f"List1 in descending order: {list4}")
# print(f"List1 in descending order: {list5}")















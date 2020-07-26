Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=[12,-7,5,64,-14]
>>> print("Original numbers in the list: ",list1)
Original numbers in the list:  [12, -7, 5, 64, -14]
>>> num = 0
>>> while(num < len(list1)):
	if list1[num] >= 0:
		print(list1[num], end=" ")
	num+=1

	
12 5 64 
>>> list2=[12,14,-95,3]
>>> print("Original numbers in the list: ",list2)
Original numbers in the list:  [12, 14, -95, 3]
>>> new_list2 = list(filter(lambda x: x >0, list2))
>>> print("Positive numbers in the list: ",new_list2)
Positive numbers in the list:  [12, 14, 3]
>>> 
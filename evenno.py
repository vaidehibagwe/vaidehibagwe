# Even no. in list
# Python program to print Even Numbers in a List 
  
# list of numbers 
list1 = [10, 21, 4, 45, 66, 93, 56, 45, 74, 86] 
num = 0
  
# using while loop         
while(num < len(list1)): 
      
    # checking condition 
    if num % 2 == 0: 
       print(list1[num], end = " ") 
      
    # increment num   
    num += 1

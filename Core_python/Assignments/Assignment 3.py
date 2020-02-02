#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q:1 Make a calculator using Python with addition , subtraction , multiplication ,division and power.                                                                                                
a = int(input("Enter 1st number  "))
b = int( input("Enter 2nd number  "))
operator = input("Enter operator  ")

if operator == "*":
    print(a*b)
    
elif operator == '+':
    print(a+b)

elif operator == '-':
    print(a-b)
    
elif operator == '/':
    print(a/b)
    
elif operator == 'p':
    print(a**b)


# In[2]:


# Q:2 Write a program to check if there is any numeric value in list using for loop
arr = [89,142,"we","power","YUP",133]
for aa in arr:
    if type(aa) == int or type(aa) == float:
        print(f"Numeric value is found = {aa} At Index={arr.index(aa)}")


# In[4]:


#Q:3 Write a Python script to add a key to a dictionary
dtio = {"firstName":"Muhammad Asad", "lastName":"Shaikh"}
print(dtio)

dtio.update({"kit":"up"})
print(dtio)


# In[7]:


#Q:3 Write a Python program to sum all the numeric items in a dictionary
result = 0
dic = {1: 2 ,
           2: "Asad", 
           3: 4.4, 
           4:"Not numerical",
           5: 99}

for value in dic.values():
    if type(value) == int or type(value) == float:
        result = result + value        
        
print(f"Sum = {result}")


# In[2]:


#Q:5 Write a program to identify duplicate values from list
the_list = ["kid", "kid", 1, 1, 0, 0.,5, 3, 4, 5, 6]
for value in the_list:
    if  the_list.count(value) > 1:
        print(f"Duplicated {value}")


# In[4]:


#Q:6 Write a Python script to check if a given key already exists in a dictionary
dic = { 1: "key1",
            2: "key2",
            3: "key3"}

given_key = 3

for key in dic.keys():
    if key == given_key:
        print(f"{given_key} Already exists")


# In[ ]:





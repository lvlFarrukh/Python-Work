#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q:01
marks=[]
totalmarks=0;
for i in range (5):
    x=int(input("enter marks out of 100"))
  
    marks.append(x)
    totalmarks=totalmarks+x

print("totalmarks =",totalmarks)  
percentage=(totalmarks*100)/500
print("percentage =",percentage)
if percentage>=90:
    print("grade A")
elif percentage>=80:
    print("grade B")
elif percentage>=70:
    print("grade C")    
elif percentage>=60:
    print("grade D") 
else:
    print("fail")


# In[3]:


#Q:2
x=int(input("enter number"))
if x%2==0:
    print("even no")
else:
    print("odd no")


# In[5]:


#Q;3
list=[15,86,29,44,49,67,70,44]
print(len(list))


# In[6]:


#Q:4
list=[69,20,38,47,99]
x=len(list)
sum=0
for i in range (x):
    sum=sum+list[i]
print("sum of list=",sum)


# In[7]:


#Q:5
list=[156,259,73,49,55]
print(max(list))


# In[8]:


#Q:6
#Less than 5
Arr = [1,12,2,3,4,5,6,7,8,10]
print("Elements less than 5 are: ",Arr[:5])


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# ## List

# In[2]:


## 1. From below list replace 4 with 44
my_list = [1, 2, 3, 4, 5]
my_list[3]=44
print(my_list)


# In[6]:


## 2. In below list add(insert) 200 at index 3
my_list = [1, 2, 3, 4, 5]
my_list.insert(3,200)
print(my_list)


# In[10]:


## 3. In below list add new number 66
my_list = [1, 2, 3, 4, 5]
my_list.append(66)
print(my_list)


# In[15]:


## 4. In below list insert new numbers 66,87,99
my_list = [1, 2, 3, 4, 5]
my_list.insert(2,66)
my_list.insert(3,87)
my_list.insert(4,99)
print(my_list)


# In[17]:


## 5. from below list remove number 3
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)


# In[20]:


## 6. From below list print count of "cherry"
my_list = [1, 2.5, "cherry", 3, "banana", 4.0, "cherry"]
my_list.count("cherry")


# In[21]:


## 7. From below list print index of "banana"
my_list = [1, 2.5, "apple", 3, "banana", 4.0, "cherry"]
my_list.index("banana")


# In[22]:


## 8. From below list remove last item
my_list = ["Pune","Delhi","Mumbai","Indore","Jaipur","Dehradun"]
my_list.pop()
print(my_list)


# In[23]:


## 9. Sort the below list in Alphabetical order
my_list = ["Grapes","Apple","Cherry","Mango","Banana"]
my_list.sort()
print(my_list)


# In[24]:


## 10. Sort below list in reverse Alphabetical order
my_list = ["Grapes","Apple","Cherry","Mango","Banana"]
my_list.sort(reverse=True)
print(my_list)


# In[3]:


# 11. Create a list named mylist that three elements:
#The integer 3
#The string 'element number two'
#Another list['last','element']
mylist = [3,'elemet',['last','element']]


# In[5]:


# 12. print the third element of the following list:
mylist = [1,2,3,4,5,6,7,8,9]
mylist[2]


# In[8]:


#13 . Modify tha last elment of this list so thats its value is 16. Print the modified list so you know the operation was performed successfully:
listtomodify = ['a','b','sixteen']
listtomodify[2]=16
print(listtomodify)


# In[9]:


#14. Calculate the length of the following list:
list = ['this','is','the','list','whose','length','i','want']
len(list)


# In[10]:


#15 . Calculate the sum of the following list :
list1 = [54,678,2878]
sum(list1)


# In[11]:


#16 . Find the maximum value of the following list :
list2 = [677,53245,234,236,23456,345,23626,3454]
max(list2)


# In[13]:


#17 . Find the minimum value of the following list :
list3 = [352,984,4354,546543,6545,876,87]
min(list3)


# In[16]:


#18 .Append the string 'append me' to the end of the following list.
list4 = [1,2,3]
list4.append('append me')
print(list4)


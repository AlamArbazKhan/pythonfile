#!/usr/bin/env python
# coding: utf-8

# In[ ]:


introduction to exceptional handeling:


# In[ ]:





# In[1]:


x = 5
y = 0

z = x/y

print(z)


# In[ ]:


try and except blocks


# In[2]:


try:
    
    x = 5
    y = 0
    z = x/y
    print(z)
except ZeroDivisionError:
    print("dont try to divide the number by zero")


# In[ ]:





# In[3]:


with open("unknown.txt") as f:
    contents = f.read()
print(contents)


# In[5]:


try:
    with open("unknown.txt") as f:
        contents = f.read()
    print(contents)
except FileNotFoundError:
    print("check the file if exists in the system or not before executing")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





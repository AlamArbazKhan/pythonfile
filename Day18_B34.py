#!/usr/bin/env python
# coding: utf-8

# In[ ]:


introduction to file hading in Python:


# In[ ]:


overview:


# In[ ]:


# Genral syntax of filehandling:


# In[ ]:


# how to read the file in python:


# In[1]:


with open('digits_B34.txt') as file_object:
    contents = file_object.read()
print(contents)


# In[ ]:


file = 'digits_B34.txt'


# In[ ]:


with open(file) as f:
    x = f.read()
print(x)


# In[ ]:





# In[ ]:


# how to write the data to the file...'digits_B34.txt'


# In[ ]:


with open(file,'w') as file_object:
    file_object.write('Python is the most demanded programming language in the global industry')


# In[ ]:





# In[ ]:


with open(file) as f:
    x = f.read()
print(x)


# In[ ]:


# how to append the data to the file


# In[ ]:


with open(file,'a') as file_object:
    file_object.write(' \n This is the right time to enter in the python industry with lot of opportunities')


# In[ ]:


with open(file) as f:
    x = f.read()
print(x)


# In[ ]:





# In[ ]:





# In[ ]:





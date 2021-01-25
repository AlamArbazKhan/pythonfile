#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Dictionary datatype:


# In[ ]:


Defination: A dict is a combination of key vvalue pairs.
    
classification : Mutable datatype
    
How to declare a dictionary: {} flower brackets or curley braces...!


# In[ ]:


Note: Most utilised datatype


# In[ ]:





# In[1]:


alien = {'color':'green','points':5}

print(alien)


# In[2]:


type(alien)


# In[ ]:





# In[3]:


# how to add new key-irsto the dictionary...

theme: 'forest'


# In[4]:


alien['theme'] = 'forest'

print(alien)


# In[ ]:





# In[ ]:


# how to access the value from the dict.


# In[5]:


print(alien['color']) # give the key and get the value in teh op.


# In[ ]:


# Req : can we give teh value and gey the op?


# In[6]:


print(alien[5]) #keyerror---->


# In[7]:


print(alien)


# In[ ]:





# In[ ]:


# facebook :

# useraccount ---->


# In[8]:


user = {'username':'codetraining01','fname':'code','lname':'training01','dod':'01-01-2019','pwd':54321}

print(user)


# In[9]:


user['checkin'] = 'Farzi cafe'


# In[10]:


print(user)


# In[11]:


user['pwd']


# In[12]:


user['pwd'] = 9876543210


# In[13]:


print(user)


# In[ ]:


# req : i want to know the firstname of the user


# In[14]:


print(user['fname'])


# In[15]:


print(user['lname'])


# In[ ]:





# In[ ]:


implimentation of for loop in a dictionary:


# In[ ]:


key,value ----> 2items


# In[ ]:


# genral syntax:

for tempvar1,tempvar2 in mainvar.items():
    print(tempvar1)
    print(tempvar2)


# In[16]:


for x,y in user.items():
    print(x)
    print(y)


# In[ ]:


# enhncement of the code....!


# In[19]:


for x,y in user.items():
    print(f"key:{x}")
    print(f"value:{y}\n")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


introduction to user accepted input:


# In[ ]:





# In[2]:


message = input("tell me somthing and i will repeat it back for you:")

print(message)


# In[ ]:





# In[3]:


name = input("please enter your name: ")

print(f"Hello, {name.title()}")


# In[ ]:





# In[ ]:


# Enhancment of the code.


# In[4]:


prompt = "if you tell us who you are, we can personalise the message for you"
prompt += "\n what is your first name" # this is the extension of the string


# In[6]:


name = input(prompt)

print(f"\nHello, {name}")


# In[ ]:





# In[ ]:


introduction to while loops:


# In[8]:


current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1 # current_number = current_number+1 = 1+1 = 2 <=5 =2+1 =3+1 = 4 <=4+1 5 = 5, 5=1 = 6,


# In[9]:


current_number = 1

while current_number <= 10:
    print(current_number)
    current_number += 1


# In[ ]:





# In[ ]:


# Letting the user choose when to quit.


# In[ ]:





# In[1]:


prompt= "\nTell me something and i will repeat it back to you"
prompt += "\nEnter 'quit' to end the program \n"


# In[2]:


message = " " # an empty string....!
while message != 'quit':
    message = input(prompt)
    print(message)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





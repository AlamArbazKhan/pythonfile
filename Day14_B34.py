#!/usr/bin/env python
# coding: utf-8

# In[ ]:


continuation to functions:


# In[ ]:


introdiction to types of arguments:
    
1. positional arguments
2. keyword arguments
3. Default arguments
4. Arbitary arguments
5. return values


# In[1]:


def describe_pet(animal_type,pet_name): # parameters # params
    """creating the function to have the details of the pet"""
    print(f"i have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name}")


# In[3]:


describe_pet('dog','bruno') # positional arguments


# In[4]:


describe_pet('rex','cat') # the same order have to be maintained in the arguments like parameters or else output will impact


# In[ ]:





# In[ ]:


# if we are changing the positions of the arguments, can we get the same output?


# In[5]:


describe_pet(pet_name='rex', animal_type = 'dog') # we are adding the parameteres as keywords here....! 
# (a different style to call the function)


# In[ ]:





# In[6]:


describe_pet('kitty')


# In[ ]:


# animal type and petname from the users....but incase of any missing information ----> 'dog'


# In[9]:


def describe_pet(animal_type = 'dog',pet_name): # parameters # params
    """creating the function to have the details of the pet"""
    print(f"i have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name}")


# In[ ]:


Note: whenever declaring the default argument keep it at the end.


# In[ ]:





# In[10]:


def describe_pet(pet_name,animal_type = 'dog'): # parameters # params
    """creating the function to have the details of the pet"""
    print(f"i have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name}")


# In[11]:


describe_pet('rex')


# In[12]:


describe_pet('cat','ray')


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





# In[ ]:





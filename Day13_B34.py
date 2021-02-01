#!/usr/bin/env python
# coding: utf-8

# In[ ]:


introduction to Functions:


# In[ ]:





# In[ ]:


understanding the concept of code reusability: **


# In[ ]:


how to define a function -------> def

# how to declare the function name ------> only small case letters


# In[ ]:


# Req: create a greet function...?


# In[2]:


def greet():
    """creating a greet function"""
    print("Hello!")


# In[3]:


greet() # CALLING THE FUNCTION OR FUNCTION CALL


# In[4]:


greet()


# In[ ]:


# create a function to greet the user....?


# In[5]:


def greetuser(username): # same input to the function defination ------> declaring the "parameteres"
    """creating the function for greeting the user""" # doc strings....
    print (f"Hello, welcome to codetraining Academy, {username.title()}")


# In[6]:


greetuser('varun') # some input during the function call ----> Argument passing


# In[7]:


greetuser('sadhana')


# In[ ]:


hello, welcome to Amazon .... yourname


# In[ ]:





# In[ ]:


# req: create a function called "Describe_pet" where in the said function needs to accept the below
# info from the user ...... "animal_type" and "pet_name"


# In[11]:


def describe_pet(animal_type,pet_name): # parameters # params
    """creating the function to have the details of the pet"""
    print(f"i have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name}")


# In[12]:


describe_pet('dog','rex') # arguments # runtime arguments # args


# In[13]:


describe_pet('cat','snowbell')


# In[ ]:





# In[ ]:


introdiction to types of arguments:
    
1. positional arguments
2. keyword arguments
3. Default arguments
4. Arbitary arguments
5. return values


# In[ ]:





# In[ ]:





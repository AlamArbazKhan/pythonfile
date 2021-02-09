#!/usr/bin/env python
# coding: utf-8

# In[ ]:


introduction to constructor (it is also called as special method or magical method):
    
overview:
    
    __init__()
    
    it will be used to intiaize the attributes in the methods...!


# In[ ]:


Req: create a dog class where it needs to have the below methods:
        
        1. Accept the name and age of the dog from the input
        
        2. jump
        
        3. sleep
        
        4. rollover
        
        5. eat
        
        6. details


# In[1]:


class Dog:
    """A simple attempt to model the dog"""
    
    def __init__(self,name,age):
        """collecting the name and age info from the user"""
        self.name = name
        self.age = age
        print("it got executed automaticalling with out calling it specifically")
        
    def jump(self):
        print(f"{self.name} is now jumping")
        
    def sleep(self):
        print(f"{self.name} is now sleeping")
        
    def rollover(self):
        print(f"{self.name} is now rolling over on the command")
        
    def eat(self):
        print(f"{self.name} is now eating")
        
    def details(self):
        print(f"{self.name} is the name of the dog")
        print(f"{self.name} is of {self.age}'s years old...!")


# In[2]:


test = Dog('scooby',2) # we can pass the arguments while assigning the objects...!


# In[3]:


test.jump()


# In[4]:


test.rollover()


# In[5]:


test.eat()


# In[6]:


test.details()


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





# In[ ]:





# In[ ]:





# In[ ]:





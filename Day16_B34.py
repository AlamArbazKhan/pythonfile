#!/usr/bin/env python
# coding: utf-8

# In[ ]:


continuation of classes 


# In[ ]:


classes:

methods:
    
attributes:
    
self:
    
objects:
    


# In[ ]:


#req: creating a greeting class:

 1. accept the input name from the user

 2. display the name

 3. greet the user
    


# In[1]:


class Greet: # class name
    """creating an greeting class""" # doc string
    
    def name(self,username): # method name (similar like the function outside of the class)
        self.username = username # attribute (similar like the variable)
        
    def display(self): # method
        print(f"{self.username}")
        
    def greetuser(self): # method...
        print(f"Hello, {self.username}")


# In[2]:


test = Greet()


# In[3]:


test.name('naveen')


# In[4]:


test.display()


# In[ ]:


# self is a temp place holder for an object


# In[ ]:





# In[5]:


asdf = Greet()


# In[6]:


asdf.name('sadhana')


# In[7]:


asdf.display()


# In[8]:


asdf.greetuser()


# In[ ]:





# In[ ]:


introduction to constructor : (it is also called as special method or magical method)
    
overview : Constructor is used to automate the method in the class and is considered as the best practise to be implimented    


# In[ ]:


how to define the constructor:
    
    def __init__(self,paraml,param2) #genric way...! initi __


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





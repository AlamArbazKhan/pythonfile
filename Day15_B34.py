#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


introduction to python classes:


# In[ ]:


Class

methods

attributes

self

object


# In[ ]:


class-----> it is an highlevel blue print design of the program that we are defining.

how to define the class ----> class

conditions to rem : we have to write the class name in the title case


# In[ ]:


methods: ----> a function written inside a class is called as method.


# In[ ]:


attribute: ----> A variable written inside the class is called as an attribute 

self: A self is a temp placeholder for an object.
        
Object: An object is an access/entry point so the class methods...!        


# In[ ]:





# In[ ]:


# req: creat a dog class and the below methods to the dog.

#

# jump

# sleep

# rollover

# details


# In[1]:


# class declartion and methods declaration:

class Dog: # class name
    """creating a class for the dog methods implimentation"""
    
    def details(self,name,age):
        self.name = name # test.name ='bruno' # attributes....
        self.age = age  # test.age = 3
        
    def jump(self):
        print(f"{self.name} is now jumping on the command")
        
    def sleep(self):
        print(f"{self.name} is now sleeing")
        
    def rollover(self):
        print(f"{self.name} is now rolling over")
        


# In[2]:


# object.methodname

# assigning the object to the class...!

test = Dog()


# In[3]:


test.details('bruno',3)


# In[4]:


test.jump()


# In[5]:


test.rollover()


# In[ ]:


# OOPS ---> Object Oriented Programming...!


# In[ ]:





# In[ ]:


# can we assign one more object to the class...?


# In[6]:


xobj = Dog() # assignmentof an object to the class or instantion of an object


# In[7]:


xobj.details('scooby',2)


# In[8]:


xobj.jump()


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





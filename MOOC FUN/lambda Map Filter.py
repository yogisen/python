
# coding: utf-8

# In[6]:


carre = lambda x: x**2-1


# In[7]:


carre(1)


# In[8]:


def image(f):
    for x in range(10):
        print(f"{f(x)}:{x}")


# In[9]:


image


# In[10]:


image(lambda x: x**2-1)


# In[11]:


image(carre)


# In[12]:


m = map (carre, range(10))


# In[13]:


m


# In[14]:


list(m)


# In[15]:


filter(lambda x: x%2 == 0, range (10))


# In[16]:


f = filter(lambda x: x%2 == 0, range (10))


# In[17]:


list (f)


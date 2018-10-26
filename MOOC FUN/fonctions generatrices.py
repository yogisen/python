
# coding: utf-8

# In[1]:


carre = [ x**2 for x in range(1000)]


# In[2]:


sum(carre)


# ### expressions generatrices

# In[3]:


carre =  (x**2 for x in range(1000))


# In[4]:


carre


# In[5]:


sum(carre)


# In[6]:


sum(carre)


# In[7]:


next(carre)


# In[8]:


gen_carre =  (x**2 for x in range(1000))


# In[9]:


palin = (x for x in gen_carre if str(x) == str(x)[::-1])


# In[10]:


list(palin)


# In[12]:


def gen():
    yield 10


# In[14]:


gen()


# In[15]:


g = gen()


# In[16]:


next(g)


# In[17]:


next(g)


# In[18]:


def gen(x):
    yield x
    x= x +1
    yield x


# In[19]:


g = gen(10)


# In[20]:


next(g)


# In[21]:


next(g)


# In[22]:


next(g)


# In[23]:


def carre(a, b):
    for i in range (a,b):
        yield i**2


# In[24]:


carre(1,10)


# In[25]:


c = carre (1, 10)


# In[26]:


list(c)


# In[28]:


def palin(it):
    for i in it:
        if (isinstance(i, (str,int))and 
           str(i) == str(i)[::-1]):
            yield i


# In[29]:


p = palin([121, 10, 12321, 'abc', 'abba'])
list(p)


# In[33]:


list(palin(x**2 for x in range(1000)))


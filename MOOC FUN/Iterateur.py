
# coding: utf-8

# In[1]:


s = { 1, 2, 3, 'a'}
for i in s:
    print (i)


# In[2]:


[x for x in s if type(x) is int]


# In[3]:


it = iter(s)


# In[4]:


it


# In[5]:


next(it)


# In[6]:


next(it)


# In[7]:


next(it)


# In[8]:


next(it)


# In[9]:


next(it)


# In[10]:


a = [1, 2]


# In[11]:


b = [3, 4]


# In[12]:


iter(a)


# In[13]:


z = zip (a, b)


# In[14]:


z


# In[15]:


z is iter(z)


# In[16]:


[i for i in z]


# In[17]:


[ i for i in z]


# In[18]:


next(z)



# coding: utf-8

# In[1]:


prenoms = [ 'ana', 'eve', 'ALICE', 'Anne', 'bob']


# In[2]:


prenoms


# In[3]:


a_prenoms = [p.lower() for p in prenoms if p.lower().startswith('a')]


# In[4]:


a_prenoms


# In[5]:


prenoms.extend(prenoms)


# In[6]:


prenoms


# In[7]:


a_prenoms = [p.lower() for p in prenoms if p.lower().startswith('a')]


# In[8]:


a_prenoms


# In[9]:


set(a_prenoms)


# In[10]:


a_prenoms =  {p.lower() for p in prenoms if p.lower().startswith('a')}


# In[11]:


a_prenoms


# In[17]:


ages = [('ana', 20), ('EVE', 30), ('Bob', 40)]


# In[18]:


ages = dict(ages)


# In[19]:


ages


# In[21]:


ages_fix = {p.lower():a for p, a in ages.items()}


# In[22]:


ages_fix


# In[23]:


ages_fix = {p.lower():a for p, a in ages.items() if a <40}


# In[24]:


ages_fix



# coding: utf-8

# In[1]:


f = open(r'c:\temp\spam.txt', 'w', encoding='utf8 ')


# In[2]:


for i in range(10):
    f.write(f"ligne {i+1}\n")


# In[3]:


f.close()


# In[4]:


get_ipython().system('type c:\\temp\\spam.txt')


# In[5]:


f = open(r'c:\temp\spam.txt', 'r', encoding='utf8 ')


# In[6]:


f2 = open(r'c:\temp\spam2.txt', 'w', encoding='utf8 ')


# In[7]:


for line in f:
    line = line.split()
    line[0] = line[0].upper()
    f2.write(".".join(line) + "\n")
    


# In[8]:


f.close()


# In[9]:


f2.close()


# In[10]:


get_ipython().system('type c:\\temp\\spam2.txt')


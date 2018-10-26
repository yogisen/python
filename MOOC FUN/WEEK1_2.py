
# coding: utf-8

# In[ ]:


dir(str)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'str')


# In[ ]:


"un mooc sur python".title()


# In[ ]:


s= "le poulet c'est bon"


# In[ ]:


s.replace('poulet', 'spam')


# In[ ]:


s = s.replace('poulet', 'spam')


# In[ ]:


s


# In[ ]:


'123'.isdecimal()


# In[ ]:


n = 'sonia'
age = 30


# In[ ]:


"{}{}".format(n, age)


# In[ ]:


f"{n} à {age} ans".title()


# In[ ]:


dir(format)


# In[ ]:


s = 'egg, bacon'


# In[ ]:


s [0]


# In[ ]:


len(s)


# In[ ]:


'egg' in s


# In[ ]:


'egg'not in s


# In[ ]:


s + ', and beans'


# In[ ]:


s.index('a')


# In[ ]:


s.count('g')


# In[ ]:


len(s)


# In[ ]:


'x'*30


# In[ ]:


s = 'abcdefghijklmnopqrstuvwxyz'


# In[ ]:


s[0:3]


# In[ ]:


s[3:]


# In[ ]:


s[:3]


# In[ ]:


s[:]


# In[ ]:


s[0:10:2]


# In[ ]:


s[0:10:1]


# In[ ]:


s[::2]


# In[ ]:


s[2::3]


# In[ ]:


s[:-3]


# In[ ]:


s[-10:-7]


# In[ ]:


s[::-1]


# ## listes
# 

# In[ ]:


a = []


# In[ ]:


type(a)


# In[ ]:


dir(list)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'list.append')


# In[ ]:


s = 'spam egg beans'
a= s.split()


# In[ ]:


a


# In[ ]:


a[0] = a[0].upper()


# In[ ]:


a


# In[ ]:


" ".join(a)


# In[ ]:


"".join(a)


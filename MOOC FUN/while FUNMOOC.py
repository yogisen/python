
# coding: utf-8

# In[ ]:


a = list(range(1,10))

while a:
    a.pop()
    print(a)


# In[ ]:


a = list(range(1,10))

while a:
    a.pop()
    if len(a) ==5:
        continue
    print(a)


# In[ ]:


a = list(range(1,10))

while a:
    a.pop()
    if len(a) ==5:
        break
    print(a)


# In[ ]:


while True:
    s = input('quelle est votre question ?\n')
    if 'aucune' in s:
        break
    


# In[ ]:


s = input('BONJOUR ?\n')
while True:
  
   
        
    if s.startswith('bonjour'):
        print("bonjour, comment allez vous")
    elif "bien" in s:
        print("c'est super !")
    elif "bye" in s:
        print ("aurevoir !")
        break
    else:
        print("mais encore")
    s = input()
    


# In[ ]:





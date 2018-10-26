
# coding: utf-8

# In[ ]:


s = input('tu veux jouer ou parler ?\n')
while True:
  
   
        
    if s.startswith('jouer'):
        print("joueons")
        
        
    elif "parler" in s:
        print("parlons !")
    elif "bye" in s:
        print ("aurevoir !")
        break
    else:
        print("mais encore")
    s = input()


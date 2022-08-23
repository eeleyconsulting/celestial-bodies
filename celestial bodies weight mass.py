#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tabulate import tabulate


# In[2]:


table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
         ["Moon",1737,73.5],["Mars",3390,641.85]]


# In[3]:


print(tabulate(table))


# In[4]:


print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))


# In[ ]:





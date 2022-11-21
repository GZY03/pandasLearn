#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[4]:


s = pd.Series([1,3,5,np.nan,6,8])


# In[5]:


s


# In[6]:


dates = pd.date_range("20130101",periods=8)


# In[7]:


dates


# In[11]:


df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("ABCD"))


# In[13]:


df


# In[17]:



# In[ ]:





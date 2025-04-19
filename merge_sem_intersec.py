#!/usr/bin/env python
# coding: utf-8

# ### Bibliotecas

# In[2]:


import pandas as pd


# ### Carregamento de dados

# In[3]:


acessos = pd.read_excel('compras_e_acessos.xlsx', sheet_name='acessos')


# In[4]:


acessos


# In[5]:


compras = pd.read_excel('compras_e_acessos.xlsx', sheet_name='compras')


# In[6]:


compras


# ### Merge sem intersecção

# #### SQL LEFT JOIN: Usuários que tem acessos, mas não tenham compras

# In[7]:


left_join = acessos.merge(compras, how='left', on='user_id', indicator=True)


# In[8]:


left_join


# In[11]:


left_join = left_join[left_join._merge == 'left_only']


# In[12]:


left_join


# #### SQL RIGHT JOIN: Usuários que têm compras, mas que não tem acessos

# In[27]:


right_join = acessos.merge(compras, how='right', on="user_id", indicator=True)


# In[28]:


right_join


# In[29]:


right_join = right_join[right_join._merge == 'right_only']


# In[30]:


right_join


# #### SQL FULL JOIN: Usuários que tem acessos OU compras, mas que não tenham os dois ao mesmo tempo

# In[31]:


full_join = acessos.merge(compras, how='outer', on='user_id', indicator=True)


# In[32]:


full_join


# In[34]:


full_join = full_join[full_join._merge != 'both']


# In[35]:


full_join


# In[ ]:





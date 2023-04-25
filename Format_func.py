#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def pld_formatter(combined):
    dcombined = combined.convert_dtypes()
    columns_comb = dcombined.columns.to_list()
    columns_comb1 = columns_comb[2:18]
    columns_comb2 = columns_comb[2:10]
    for x in columns_comb1:
        dcombined[x] = dcombined[x].astype(float)
    for a in columns_comb2:
        dcombined[a] = dcombined[a]/10
    dcombined
    x = dcombined["Calendar"].str.split("|", expand = True)
    x = x.astype(int)
    x = x[0]+x[1]+x[2]
    dcombined["Calendar"] = x/(60*60*24) + 25569
    dcombined = dcombined.drop(["Axis Item"], axis = 1)
    return dcombined


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This will combine csv file from a file list
#File list from a pandas data frame
#convert Pandas data frame of file path/directory into list (to_list)

import pandas as pd 

def pld_combiner(pandas_file_list):
    combine_data = []
    for y in pandas_file_list:  
        ff_1 = str(y[0]).replace('[','') #pn_1 = single path name
        ff_1 = ff_1.replace(']','') # string moification
        ff_1 = ff_1.replace("'","") # string moification
        sing_data = pd.read_csv(filepath_or_buffer = ff_1, engine = "c")
        sing_data = pd.DataFrame(sing_data)
        combine_data.append(sing_data)
    combined = pd.concat(combine_data)
    combined2 = combined.drop_duplicates()
    #combined1 = combined.drop_duplicates(subset = ["Calendar"] , keep = "last")
    #combined1["Calendar"].duplicated().sum()
    return combined2


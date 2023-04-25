#!/usr/bin/env python
# coding: utf-8

# In[2]:

import os
import time
from datetime import datetime
import pandas as pd

def list_files(dir):                                                                                                  
    r = []
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).__next__()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(os.path.join(subdir, file))                                                                         
    return r

def file_att_implementor(file_list):
    modified_time = []
    folder_time = []
    machine_serial = []
    file_name = []
    for x in file_list:
        pn_1 = str(x[0]).replace('[','') #pn_1 = single path name
        pn_1 = pn_1.replace(']','') # string moification
        pn_1 = pn_1.replace("'","") # string moification
        mtime = os.path.getmtime(pn_1) #mtime = modified time
        mtime = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')#convert seconds into readable date
        modified_time.append(mtime) #add the mtime into the modified time list
        ftime = pn_1.split("\\")
        ftime = ftime[-3]
        folder_time.append(ftime)
        ms = pn_1.split("\\")
        ms = ms[-4]
        machine_serial.append(ms)
        file_name.append(os.path.basename(pn_1).split('\\')[-1])
        file_org = pd.DataFrame(list(zip(file_list, modified_time, folder_time, machine_serial, file_name)))
        file_org = file_org.sort_values(by = 2, ascending = False)
        file_org.rename(columns = {0:"File Path",
                                   1:"Modified Time",
                                   2:"Folder Name Time",
                                   3:"Machine Serial No.",
                                  4: "File Name"}, inplace = True)
    return(file_org)


# In[ ]:





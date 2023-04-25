#!/usr/bin/env python
# coding: utf-8

# In[1]:


class AskInput:
    def __init__(self, inputlength, mes1, mes2, mes3 ):
        self.mes1 = mes1
        self.mes2 = mes2
        self.inputlength = inputlength
        self.mes3 = mes3
    def input_num(self):
        state_input = False
        while not state_input:
            input_fig = input(self.mes1)
            if len(input_fig) != self.inputlength:
                print(self.mes2)
            else:
                try:
                    date = int(input_fig)
                except:
                    ValueError = print(self.mes3)
                else:
                    return input_fig


# In[ ]:





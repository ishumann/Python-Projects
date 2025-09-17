# %% [markdown]
#create List [DI
# Len IDI I
# append IDI
# print [DI
# indexing [DI
# pop [DI
# clear [DI
# find [DI
# insert TDI
# delete IDI
# remove IDI
# sort/min/max/sum
# extend
# negative indexing
# slicing
# Merge
# %%
import ctypes
class MeraList:
    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size  = self.size
        self.A = self.__make_array(self.size)
    def __len__(self):
        return self.n

    def __make_array(self, capacity):

        # create a C type array(Static, referential) with size  = capacity

        return(capacity*ctypes.py_object)()
    
    
    def __append__(self, ele):
        

L = MeraList()

len(L)
# %%

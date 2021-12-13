#!/usr/bin/env python
# coding: utf-8

# In[1]:


class mul():
       def pow(self, x, n):
        if x==0:
            return x 
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(mul().pow(10, 2));


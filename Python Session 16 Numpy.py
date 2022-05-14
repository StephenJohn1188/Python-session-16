#!/usr/bin/env python
# coding: utf-8

# # Numpy

# In[1]:


import numpy


# In[4]:


numpy.array([1,2,3,4,5,6,7,8,9])


# In[5]:


numpy.array([10,20,30,40,50,60,70,80,90])


# In[7]:


a=numpy.array([10,20,30,40,50,60,70,80,90])


# In[9]:


a


# In[10]:


b=numpy.array([1,2,3,4,5,6,7,8,9])


# In[11]:


b


# In[12]:


import numpy as np


# In[13]:


a


# In[14]:


c=np.array([1.1,2.2,3.3,4.4])


# In[15]:


c


# In[16]:


a.size


# In[17]:


b.size


# In[18]:


c.size


# In[19]:


a.shape


# In[20]:


b.shape


# In[21]:


c.shape


# In[22]:


d=np.array([[10,20],[30,40]])


# In[23]:


d


# In[29]:


d.size


# In[30]:


d.shape


# In[33]:


e=np.array([[1,2,3],[7,8,9],[4,5,6]])


# In[34]:


e


# In[35]:


e.size


# In[36]:


e.shape


# In[46]:


f=np.array([[1,2,3,4],[7,8,9,10],[4,5,6,7],[11,12,13,14]])


# In[40]:


f


# In[41]:


f.size


# In[42]:


f.shape


# In[47]:


j=np.array([[1,2,3,4],[7,8,9,10],[4,5,6,7]])


# In[48]:


j


# In[49]:


j.shape


# In[50]:


j.reshape(4,3)


# In[52]:


j.min()


# In[53]:


j.max()


# In[54]:


f.dtype


# In[56]:


j.size


# In[57]:


j.itemsize


# In[59]:


k=np.array([[1.1,2.2,3.3],[4.4,5.5,6.6]],dtype='float64')


# In[61]:


k


# In[62]:


k.itemsize


# In[63]:


k.dtype


# In[64]:


k.ndim


# In[69]:


#to use a sequence of integer use arange fn


# In[65]:


l=np.arange(5)


# In[66]:


l


# In[67]:


m=np.arange(15)


# In[70]:


m


# In[71]:


o=np.arange(25)


# In[72]:


print(o)


# In[74]:


p=np.arange(24).reshape(6,4)


# In[75]:


p


# In[77]:


print(p.ravel())


# In[79]:


np.arange(0,10)


# In[80]:


#Skipping integers in array
np.arange(0,10,2)


# Broadcasting in Numpy
# 

# In[81]:


a*b


# In[84]:


a=numpy.array([10,20,30,40,50,60,70,80,90])
q=2.4
a*q


# In[86]:


e=np.array([[1,2,3],[7,8,9],[4,5,6]])
q=2.4
e*q


# In[88]:


e**2


# In[89]:


e=np.random.random([2,3])


# In[90]:


e


# In[91]:


c=np.ones([2,3])


# In[92]:


c


# In[93]:


r=e+c


# In[94]:


r


# Universal Functions

# In[95]:


s=np.arange(6)


# In[96]:


s


# In[97]:


np.exp(s)


# In[98]:


np.sqrt(s)


# In[102]:


c=np.array([7,8,9,10,11,12])
np.add(s,c)


# Indexing, Slicing and Iterating

# In[103]:


a=np.arange(10)


# In[104]:


a


# In[105]:


a[2]


# In[106]:


a[2:5]


# In[107]:


a[-2]


# In[108]:


a[-4]


# In[109]:


a[-4:]


# In[110]:


a[-4:-2]


# In[111]:


d2=np.arange(20)


# In[112]:


d2


# In[113]:


d2[5:]


# In[114]:


d3=np.array([np.nan,1,2,3,np.nan,4,5,6])


# In[115]:


d3


# In[116]:


np.random.rand(2,3)


# In[117]:


np.random.randn(2,3)


# In[ ]:





# In[ ]:





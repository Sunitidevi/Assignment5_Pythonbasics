#!/usr/bin/env python
# coding: utf-8
1.What does an empty dictionary's code look like?
# In[2]:


d={}
type(d)
d=dict()
type(d)

2.what is the value of dictionary value with key 'foo' and the value 42 ?
# In[9]:


d={'foo':42}
print(d.values())
print(d.keys())

3.What is the most significant distinction between a dictionary and a list?list[] has ordered items and Dict {} has unordered items.4.What happens if you try to access spam ['foo'] if spam is {'bar':100} ?
# In[10]:


spam={'bar':100}
spam['foo']#key error will be found

5.if a dictionary is stored in spam,what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys() ?Same7.what is a shortcut for the following code ?
if 'color' not in spam: spam['color'] ='black'
# In[11]:


spam.setdefault('color','black')

8.How do you 'pretty print' dictionary values using which modules and function ?
# In[ ]:


Using pprint module and pprint()function.


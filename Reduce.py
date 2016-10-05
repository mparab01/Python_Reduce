
# coding: utf-8

# Built-In Function in Python : Reduce

# Q. Find the Max number

# In[35]:

max_find = lambda a,b : a if (a>b) else b


# In[36]:

max_find(49, 50)


# In[37]:

l = range(51)


# In[38]:

print l


# In[39]:

l.reverse()


# In[40]:

red = reduce(max_find, l)
print red


# Q.2. 

# In[41]:

e = range(10)
print e
add = (lambda x,y : x+y)
p = reduce(add, e)
print "Addition of first 10 numbers : ", p


# In[ ]:




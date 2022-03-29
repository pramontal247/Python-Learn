#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Day 1 python re-learning


num = 36
name = 'phil'

print('My name is {one} and my number is {two}'.format(one = num, two = name))


# In[7]:


s = 'hello'

s[4]


# In[8]:


#indexing

s = 'abcdefghijk'


# In[11]:


s[3:6]


# In[16]:


# list

[1,2,3]

my_list = ['a','b','c']

my_list.append('d')


# In[17]:


my_list


# In[19]:


my_list[1]


# In[20]:


my_list[1] = 'Phil'


# In[21]:


my_list


# In[23]:


nested = [1,2,[3,4]]

nested[2][0]


# In[25]:


nest = [1,2,3,[4,5,["target"]]]


print(nest[3][2][0])


# In[28]:


# Dictionary

d = {'key1':'value', 'key2':'123'}
     
print(d['key1'])  


# In[32]:


d = {'k1':[1,2,3]}
d['k1'][2]


# In[33]:


d = {'k1':{'inner':[1,2,3]}}


# In[34]:


d['k1']['inner'][1]


# In[35]:


set([1,1,12,2,23,3,3,4,4,5,5])


# In[36]:


s = {1,2,3}

s.add(4)


# In[37]:


s


# In[38]:


1>2


# In[40]:


1<2


# In[41]:


2 == 2


# In[42]:


3 == 4


# In[43]:


(1 < 2) and (2 < 3)


# In[44]:


if 1 < 2:
    print('True')


# In[50]:


if 1 == 2:
    print('first')
elif 4 == 4:
    print('first')
elif 3 ==  3:
    print('sec')
else:
    print('last')
    


# In[52]:


# For loops

seq = [1,2,3,4,5]

for item in seq:
    print(item)


# In[3]:


i = 1

while i < 5:
    print('i is: {}'.format(i))
    i = i + 1


# In[4]:


x = [1,2,3,4]

out = []

for num in x:
    out.append(num*2)

    
print(out)
    


# In[5]:


# list comprehension

[num* 2 for num in x]


# In[23]:


def my_func(name = 'phil'):
    print('hello ' + name)


# In[24]:


my_func()


# In[25]:


def square (num):
    return num * 4


# In[26]:


output = square(4)
output


# In[30]:


# map

def times2(var):
          return var*3


seq = [1,2,3,4,5,6]

list(map(times2,seq))


# In[31]:


# lambda

p = lambda var:var*5

p(10)


# In[33]:


list(filter(lambda num: num%2 ==0, seq))


# In[34]:


s = 'My name is Phil'


# In[35]:


s.split()


# In[37]:


tweet = 'Go Sports!#Sports'
tweet.split('#')[0]


# In[38]:


#tuple unpacking

x = [(1,2), (3,4), (5,6)]


# In[39]:


x


# In[41]:


for (a,b) in x:
    print(b)


# In[ ]:





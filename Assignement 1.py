#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task 1 Q1
print ('Hello World')


# In[5]:


# Task 1 Q2
i = 2000
while i <= 3200:
    i=i+1
    if i % 7 == 0:
        if i % 5 != 0:
           print (i,end=',')

        
    


# In[6]:


# Task1 Q3
fname = input("What is your first name?")
lname = input("What is your last name? ")
fname = fname[::-1]
lname = lname[::-1]
print ('your name in reverse order is : ',fname+' '+lname  )


# In[8]:


# Task1 Q4
d = 12
r = d/2
v = (4/3) * (22/7) * (r**3)
print('volume for sphere is : ', v)


# In[11]:


# Task 2 Q1
n = input('enter a series of comma separated numbers : ')
i = len(n)
print(i)
# remove comma's in the string
n=n.replace(',','')
print(n)
# typecast string to list
n=list(n)
print(n)


# In[13]:


# Task 2 Q2
for i in range(6):
    v='*'
    j=i*v
    print(j)
    if i==5:
        for k in range(6):
            q=6-k
            h=q*v
            print(h)


# In[15]:


#Task 2 Q3
word = input('Enter a word to be reversed : ')
print('The reversed word is: ',word[::-1])


# In[32]:


#Task 3 Q4
word = "WE, THE PEOPLE OF INDIA,{}having solemnly resolved to constitute India into a SOVEREIGN,{}SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC{} and to secure to all its citizens"
print (word.format('\n\t','!\n\t\t','\n\t\t'))


# In[ ]:





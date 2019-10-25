#面试题21:调整数组顺序使奇数位于偶数前面



import random 
a=[]
for i in range(10):
    a.append(random.randint(1,100))
b=[]
for i in range(len(a)):
    if(i%2==0):
        b.append(a[i])
for i in range(len(a)):
    if(i%2==1):
        b.append(a[i])
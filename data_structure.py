# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:10:35 2019

@author: 陈彪
版权所有，翻版必究
"""


#两个有序链接的合并,下面的算法是有序链表的合并，使用的是
import random 

def arrays(n):
    a=[]
    for i in range(n):
        a.append(random.randint(0,100))
    a.sort()
    return a

def addarrays(a,b):
    c=[]
    i=0
    j=0
    while (i<len(a) and j<len(b)):
        if(a[i]<b[j]):
            c.append(a[i])
            i=i+1
        else:
            c.append(b[j])
            j=j+1
    
    if(i<len(a)):
        c=c+a[i:len(a)]
    else:
        c=c+b[j:len(b)]
    return c
        
if __name__=="__main__":
    #使用空格格式化输入两个正整数，分别作为两个list的长度
    #a,b的长度都不能是空值
    a=list(map(int,input().split(' ')))
    m,n=a[0],a[1]
    a=arrays(m)
    b=arrays(n)
    c=addarrays(a,b)
    print(a)
    print(b)
    print(c)
    
    
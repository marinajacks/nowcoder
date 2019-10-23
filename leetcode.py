#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:38:41 2019

@author: macbook
这个是leetcode上的一些题目的求解，自己就把这个当成草稿纸一样来进行书写。
"""

#7.整数反转
def reverse(x) -> int:
        if (x==0 or x>(pow(2,31)-1) or x<(-pow(2,31))):
            return 0
        else:
            a=list(str(x))

            if a[0]=='-':
                b=''
                del a[0]
                a.reverse()
                while a[0]=='0':
                    del a[0]
                for i in a:
                    b=b+i
                b=int('-'+b)
                if(b>pow(2,31)-1 or b<-pow(2,31)):
                    b=0
            else:
                b=''
                a.reverse()
                while a[0]=='0':
                    del a[0]
                for i in a:
                    b=b+i
                b=int(b)
                if(b>pow(2,31)-1 or b<-pow(2,31)):
                    b=0
        return b

if __name__=="__main__":
    x=int(input())
    print(reverse(x))
    
#8.字符串转换整数（atoi)
    
    
    x="-1920"
    a=list(x.strip())
    if(a[0]=='-'):
        
        
        
        
        
def test(a,b,n):
    c=[]
    
    d=[] 
    for i in range(n):
     
        d.append(a)
        
    
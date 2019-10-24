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
    
def test3(x):
    a=list(x.strip())
    b=""
    if(len(a)>0):
        if(a[0]=='-'):
            b=b+a[0]
            del a[0]
            for i in range(len(a)):
                b=b+a[i]
                if(a[i].isdigit()==False):
                    b=b[0:-1]
                    break
        elif (a[0].isdigit()):
            for i in range(len(a)):
                b=b+a[i]
                if(a[i].isdigit()==False):
                    b=b[0:-1]
                    break
        else:
            b=0
    else:
        b=0
    b=int(b)
    if(b>pow(2,31)-1):
        b=pow(2,31)-1
    if(b<-pow(2,31)):
        b=-pow(2,31)
    
    return b 
        

#17.电话号码的字母组合
    
def sctip17(a):
    c=[]
    if(a==2):
        c-'a','b','c']
    elif(a==3)
        case 2:
            c=['a','b','c']
        case 3:
            c=['d','e','f']
            
    
    return c


        
        
        
    
    
        
    
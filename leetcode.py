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
        c=['a','b','c']
    elif(a==3):
        c=['d','e','f']
    elif(a==4):
        c=['g','h','i']
    elif(a==5):
        c=['j','k','l']
    elif(a==6):
        c=['m','n','o']
    elif(a==7):
        c=['p','q','r','s']
    elif(a==8):
        c=['t','u','v']
    elif(a==9):
        c=['w','x','y','z']
    else:
        c=[]
    return c

def test17(a):
    b=list(a)


#子字符串的位置判定            
def strStr( haystack, needle):
    import re
    a=re.search(needle,haystack)
    if(a is None):
        return -1
    else:
        return a.span()[0]
        
    
#54 螺旋矩阵
'''
螺旋矩阵的问题，我们需要对这个问题进行分析，了解哪些这个圈层的整体
情况，从而通过分析，找到一般的特点，最后完成对应的分析。
1.首先，我们分析，这种螺旋矩阵的道路走的特点一般是每次完成一个圈层的
循环，然后再完成另一个圈层的循环。可以看到，每次都是一层的运动。
2.层数和矩阵的m和n有关系，无论m和n是怎么样的，圈层的个数都是和m和n的
最小数有关。而且层数和上面的最小数的奇偶性有关，如果是奇数，那么层数就
是这个数的一半的取整然后再加上1即可，否则就是直接取这个数据的一半。
3.在顺序上，数据在旋转的过程中，主要是有4个步骤，分别是:右向增加;下向增加;
左向减小;向上减小。这是一圈的过程。这里有一个点需要注意，首先就是对于每
圈的两个重点，需要注意的是每圈两边都需要注意，初始值每圈要增加一，终端值
每次要减小一。对于每一圈，第一路是横坐标不变，纵坐标增加；第二路是纵坐标
不变，横坐标增加；第三路是横坐标不变，纵坐标减小；地思路是纵坐标不变，横坐
标减小。另外每一层开始值加上层数，终止值减去层数。
4.对于层数是奇数和偶数的区别，如果是偶数，那么就是每一圈一直实现到终结；对
于奇数，最后一层只实现第一个横向增加即可。
'''
def test(m,n):
    a=[]
    for i in range(m):
        b=[]
        for j in range(n):
            b.append(i*n+j+1)
        a.append(b)
    return a   
def test54(a):
    height=len(a)
    width=len(a[0])
    d=min(height,width)
    result=[]
    if(d%2==0):
        k=0
        while(k<d/2):
            i=k
            for j in range(k,len(a[i])-k):
                print(a[i][j])
                result.append(a[i][j])
            for i in range(1+k,height-k):
                print(a[i][j])
                result.append(a[i][j])
            for j in range(width-1-1-k,-1+k,-1):
                print(a[i][j])
                result.append(a[i][j])
            for i in range(height-1-1-k,0+k,-1):
                print(a[i][j])
                result.append(a[i][j])
            k=k+1
    else:
        k=0
        while(k<(d-1)/2):
            i=k
            for j in range(k,len(a[i])-k):
                print(a[i][j])
                result.append(a[i][j])
            for i in range(1+k,height-k):
                print(a[i][j])
                result.append(a[i][j])
            for j in range(width-1-1-k,-1+k,-1):
                print(a[i][j])
                result.append(a[i][j])
            for i in range(height-1-1-k,0+k,-1):
                print(a[i][j])
                result.append(a[i][j])
            k=k+1
        i=k
        for j in range(k,len(a[i])-k):
            print(a[i][j])
            result.append(a[i][j])
    return result
    

#这个和上面的一样,都是螺旋矩阵
    def spiralOrder(matrix):
        height=len(matrix)
        width=len(matrix[0])
        d=min(width,height)
        result=[]
        if(d%2==0):
            k=0
            while (k<d/2):
                i=k
                for j in range(k,width-k):
                    result.append(matrix[i][j])
                for i in range(k+1,height-k):
                    result.append(matrix[i][j])
                for j in range(width-2-k,k-1,-1):
                    result.append(matrix[i][j])
                for i in range(height-2-k,k,-1):
                    result.append(matrix[i][j])
                k=k+1
        else:
            k=0
            while k<(d-1)/2:
                i=k
                for j in range(k,width-k):
                    result.append(matrix[i][j])
                for i in range(k+1,height-k):
                    result.append(matrix[i][j])
                for j in range(width-2-k,k-1,-1):
                    result.append(matrix[i][j])
                for i in range(height-2-k,k,-1):
                    result.append(matrix[i][j])
                k=k+1
            i=k
            for j in range(k,width-k):
                result.append(matrix[i][j])
        return result
    
    
#118题,计算杨辉三角
def generate(numRows):
    result=[]
    for i in range(numRows):
        temp=[]
        for j in range(i+1):
            if(i==j or j==0):
                temp.append(1)
            else:
                temp.append(result[i-1][j-1]+result[i-1][j])
        result.append(temp)
    return result
    

#119题,返回杨辉三角的最后一行
def getRow( rowIndex):
    result=[]
    for i in range(rowIndex):
        temp=[]
        for j in range(i+1):
            if(j==0 or i==j):
                temp.append(1)
            else:
                temp.append(result[i-1][j]+result[i-1][j-1])
        result.append(temp)
    return result[rowIndex-1]


#120题 三角形最小路径和
a=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
def minimumTotal(triangle):
    result=[a[0][0]]
    index=0
    for i in range(1,len(a)):
        if(index==0):
            index0=0
            for j in range(index,index+2):
                if(a[i][index0]>a[i][j]):
                    index0=j
            index=index0
            result.append(a[i][index])
        else:
            index0=index-1
            for j in range(index-1,index+2):
                if(a[i][index0]>a[i][j]):
                    index0=j
            index=index0
            result.append(a[i][index])
    return sum(result)
            

#判断一个输入的字符串是不是对称的
def digitandalpha(s):
    strs=list(s.lower())
    strss=[]
    for i in range(len(strs)):
        if(strs[i].isdigit() or strs[i].isalpha()):
            strss.append(strs[i])
    
    lens=int(len(strss)/2)
    flag=True
    for i in range(lens):
        if(strss[i]!=strss[len(strss)-1-i]):
            flag=False
            break
        
    return flag

if __name__=="__main__":
    s=input()
    print(digitandalpha(s))
    
    

    
#两个二进制的数相加，处理思路是，使用字符串，
#反转的方式，从低级
def binadd(a,b):
    a1=list(a)
    a1.reverse()
    b1=list(b)

        else:
            c.append(a[i]+b[i])
            
            
            
#
    

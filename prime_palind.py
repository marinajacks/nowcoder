# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 09:10:51 2019

@author: hello
问题要求，给定一个区间，判断这个区间中既是回文数又是素数的数。
1.回文数。所谓回文数，就是这个数正过来读和反过来读都是一样的数，例如121就是一个回文数，但是
132就不是一个回文数。
2.素数。素数就是除了1和它自身之外没有其他的因子的数就是素数。例如2,3,5这些都是素数，但是6因
为有1,2,3,6等四个因子，所以这个数不是素数。
3.我们这里判断一个数既是回文数又是素数，例如131就满足这两个条件，然后我们需要注意的是，现在
的区间是100到150之间，那个这个区间中的回文数有两个，所以返回的结果是2.
"""
import math
'''判断一个是不是素数，基本的处理思路是，只要计算从2到这个数的算术平方根的中是不是存在这个
数的因子即可，如果有的话这个数就不是素数，否则就是。
'''
def isprime(a):
    flag=True
    b=int(math.sqrt(a))
    for i in range(2,b+1):
        if(a%i==0):
            flag=False
            break
    return flag



'''基本处理方式是将int型的数字转化成字符转，判断字符串是不是堆成的即可。虽然这个问题没有完全考
虑到某些边界条件
''' 
def palind(a):
    b=list(str(a))
    lens=int(len(b)/2)
    flag=True
    for i in range(lens):
        if(b[i]!=b[len(b)-i-1]):
            flag=False
            break
    return flag
#同时判断这个数是不是素数和回文数，如果都满足的话才算是满足要求的数，否则就不是
def test(a,b):
    nums=0
    for i in range(a,b+1):
        if(isprime(i)==True and palind(i)==True):
            nums=nums+1
    return nums
     
#主函数直接格式化输入即可   
if __name__=="__main__":
    a=list(map(int,input().split(' ')))
    print(test(a[0],a[1]))
    

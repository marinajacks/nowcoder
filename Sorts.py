# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:52:56 2019

@author: 陈彪，版权所有

这个是一个排序算法的总结，将所有的排序算法都重新写一遍，然后我们首先会分析算法的时间
复杂度，然后简单介绍一下这些算法的原理，最后使用python实现，然后我们会使用测试案例
来进行测试。

"""

import random 

'''首先映入眼帘的就是冒泡排序，这是一个让人理解起来最简单的排序算法，这个算法的时间复
杂度是O(N^2),从下面的程序中也能看出来这个算法的时间复杂度确实是O(N^2).

'''
def bubble(a):
    for i in range(len(a)):
        for j in range(i,len(a)):
            if(a[i]>a[j]):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    return a








if __name__=="__main__":
    a=[]
    for i in range(10):
        a.append(random.randint(10,40))
    print(a)
    print(bubble(a))
    print('hello world!')
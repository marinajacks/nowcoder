# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:20:55 2019

@author: hello

现在有一个问题主要是对两个有序数组进行合并，现在假设有两个数组都是单调递增的数组，
那么如何将这个问题进行处理呢，我们的思路是什么呢。基本的思路是。既然我们已经假设
两个数组是有序的，那么现阶段就有两种处理的方法。第一种是，直接将第二个数组加入到
第一个数组中，然后排序即可。

"""
def merge(a,b):
    c=a+b
    c.sort()
    return c
    


'''
这种方式就是在第一种
'''
def merge1(a,b):
    
    
    
    
    return 0
    
    
    
    
    
if __name__=='__main__':
    a=[10, 10, 17, 18, 19, 20]
    b=[10, 16, 29, 33, 38]
    a.extend(b)
    print(merge(a,b))
    
    
    
    
    
    
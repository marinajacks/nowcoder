# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:20:55 2019

@author: 陈彪，版权所有

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
这种方式就是在第一种的扩展板，主要处理的方式是，首先判断数组a和b的第一个元素的大小，
然后根据第一个元素的大小来判断是将一个数组中的元素填入第二个还是将第二个数组中的元素
填入第一个数组，在这个过程中，还要判断最后一个元素对整体的影响。例如，如果第一个数组
数组某个元素已经大于第二个元素的最后一个元素，那么就将这个元素后边的全部加到第二个数组
末尾即可。下面的这个程序驾驶的是数组是按照从小到大排列的。
'''
def merge1(a,b):
    if(a[0]>b[0]):
        while len(a)>0:
            for i in range(len(b)-1):
                if(a[0]>b[len(b)-1]):
                    b.extend(a)
                    a=[]
                    break
                if (a[0]>=b[i] and a[0]<=b[i+1]):
                    b.insert(i+1,a[0])
                    del a[0]
                    break
        return b

    else:
        while len(b)>0:
            for i in range(len(a)-1):
                if(b[0]>a[len(a)-1]):
                    a.extend(b)
                    b=[]
                    break
                if (b[0]>=a[i] and b[0]<=a[i+1]):
                    a.insert(i+1,b[0])
                    del b[0]
                    break
        return a

if __name__=='__main__':
    a=[10, 10, 17, 18, 19, 20]
    b=[10, 16, 29, 33, 38]
    print(merge(a,b))
    
    a=[19, 21, 30, 32, 33]
    b=[14, 25, 29, 32, 38, 39]
    print(merge1(a,b))
    
    
    
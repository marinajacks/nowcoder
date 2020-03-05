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
def arrayss(n):
    a=[]
    for i in range(n):
        a.append(random.randint(0,100))
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
        
#if __name__=="__main__":
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
    



'''在下面我们会对几个排序算法进行复习，尤其是几个关键的排序算法，例如：冒泡排序，选择排序，
插入排序，归并排序、快速排序和堆排序等相关的排序算法。我们需要对这些算法的时间复杂度和空间
复杂度以及对应的算法的实现进行一番的分析和相关的介绍。
'''
#快速排序
'''
快速排序是一个经典的使用分治+递归的方式来求解的方式，这个方式的主要处理方法是。
首先，找到一个标识，假设这个标识是第一个元素，我们以这个数作为标准，对整个数组进行排序。
设置两个指针，分别是从前出发left和从后出发的标签right，标识数据位置的指针。
1.从数组最后一位出发，找到比这个标签小的第一个数据，将右边的指针right指向该位置；
2.从数组的第一位出发，找到比这个标签大的第一个数据，将左边的指针left指向该位置；
3.如果lfet和right仅仅相差1，那么就将最初的那个标识放到中间。
分别对左边部分和右边部分重复上面的快速排序算法。指导子数组的长度仅仅为1为止。
'''

def quicksort(data):
    if(len(data)>=2):
        flag=data[0]
        left,right=[],[]
        data.remove(flag)
        for num in data:
            if num>=flag:
                right.append(num)
            else:
                left.append(num)
        return quicksort(left)+[flag]+quicksort(right)
    else:
        return data
    
'''
下面是非常简单的冒泡排序,至于这个算法的实现是一件十分简单的事情，就是比较
一个数和它后边的一些数的大小，类似冒泡的过程。
'''
def bubble(data):
    for i in range(len(data)):
        for j in range(i,len(data)):
            if(data[i]>data[j]):
                temp=data[i]
                data[i]=data[j]
                data[j]=temp
    
        
#下面是选择排序，我们对这个算法进行实现
'''
选择排序的是实现是这样的，从第1个数据开始，从后边的所有的

'''
def choosesort(data):
    j=0
    while (j<len(data)):
        flag=j
        for i in range(j+1,len(data)):
            if(data[flag]>data[i]):
                flag=i
                
        temp=data[flag]
        data[flag]=data[j]
        data[j]=temp
        j=j+1


#下面是插入排序，所谓插入排序就是，对后面每一个元素的数据，根据它在前面的位置，将其
#插入到合适的位置上。
        
def insertsort(data):
    
    
    return 0
        
        
if __name__=="__main__":
    a=arrayss(10)
    print(a)
    print(quicksort(a))
    
        
    
    
class ListNode:
    def __init__(self, x):
       self.val = x     
       self.next = None
       
       
       
       
def sorts(a,left,right):
    l=left
    r=right




import math 
def zips(a):
    b=[]
    for i in range(len(a)):
        b.append(math.sqrt(pow(a[i][0],2)+pow(a[i][1],2)))
    return dict(zip(a,b))





def merge(nums1, nums2):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i=0
    j=0
    result=[]
    while (i<len(nums1) and j<len(nums2)):
        if(nums1[i]<nums2[j]):
            result.append(nums1[i])
            i=i+1
        else:
            result.append(nums2[j])
            j=j+1
        
    if(i<len(nums1)):
        result=result+nums1[i:len(nums1)]
    else:
        result=result+nums2[j:len(nums2)]
    return result



def merge(nums1, m, nums2 ,n):
    i=0
    j=0
    result=[]
    while (i<m and j<n):
        if(nums1[i]<nums2[j]):
            result.append(nums1[i])
            i=i+1
        else:
            result.append(nums2[j])
            j=j+1
        
    if i<m:
        result=result+nums1[i:len(nums1)]
    else:
        result=result+nums2[j:len(nums2)]
    return result
                     





def box_2_kitti_format(box):
    '''Transform box for KITTI label format'''
    x = box[0]
    y = box[1]
    w = box[2]
    h = box[3]
    left = int(x - w/2)
    right = int(x + w/2)
    top = int(y - h/2)
    bot = int(y + h/2)
    return [left,top,right,bot]

def kitti_2_box_format(label):

    '''Transform KITTI label format to box'''
    xl = label[0]
    yt = label[1]
    xr = label[2]
    yb = label[3]
    w = xr - xl
    h = yb - yt
    xc = int(xl + w/2)
    yc = int(yt + h/2)
    return [xc, yc, w, h]


def iou(box1, box2):
  """Compute the Intersection-Over-Union of two given boxes.

  Args:
    box1: array of 4 elements [cx, cy, width, height].
    box2: same as above
  Returns:
    iou: a float number in range [0, 1]. iou of the two boxes.
  """

  lr = min(box1[0]+0.5*box1[2], box2[0]+0.5*box2[2]) - \
      max(box1[0]-0.5*box1[2], box2[0]-0.5*box2[2])
  if lr > 0:
    tb = min(box1[1]+0.5*box1[3], box2[1]+0.5*box2[3]) - \
        max(box1[1]-0.5*box1[3], box2[1]-0.5*box2[3])
    if tb > 0:
      intersection = tb*lr
      union = box1[2]*box1[3]+box2[2]*box2[3]-intersection

      return intersection/union

  return 0



x=[542.05 ,175.55, 565.27 ,193.79]
y=[525.7 ,174.1, 549.7, 191.7]
z=[564.62 ,174.59, 616.43, 224.74]

x1=kitti_2_box_format(z)

y1=kitti_2_box_format(y)
 
print(iou(x1,y1))



p='D:\project\服务器\detection_files_2000\error_analysis\det_error_file.txt'

f=open(p,'r')


lines=f.readlines()

locs=[]

for line in lines:
    if 'loc' in line:
        locs.append(line.strip().split(' '))
        print(line)
        
    

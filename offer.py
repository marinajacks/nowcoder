#面试题21:调整数组顺序使奇数位于偶数前面
def ReOrder(a):
    b=[]
    for i in range(len(a)):
        if(i%2==0):
            b.append(a[i])
    for i in range(len(a)):
        if(i%2==1):
            b.append(a[i])
    return b



#面试题11：旋转数组的最小数字
'''这个问题有几种情况，第一种就是这种求最大或者是最小值的。这里可以设定是最大值或者是
最小值。另外的一些情况就是，求任意一个数值的index,这个需要注意，算是前面那种问题的推
广大。首先，我们会

'''

import random
def createarray(m,n):
    a=[]
    for i in range(m):
        a.append(random.randint(1,100))
    a.sort()
    b=a[n:len(a)]+a[0:n]
    return b 

def test(a):
    left=0
    right=len(a)-1
    mid=int((left+right)/2)
    if(a[left]>a[right]):
        while(left<right-1):
            if(a[mid]>a[right]):
                left=mid
            else:
                right=mid
            mid=int((left+right)/2)
        return right
    else:
        while(left<right-1):
            if(a[mid]>a[right]):
                right=mid
            else:
                left=mid
            mid=int((left+right)/2)
        return left
    
    
#牛课上的剑指offer上的爬楼梯问题，这个问题主要的思路是维护一
#个数组，从而实现数据的非重复。
def test23(n):
    a=[0,1,2]
    for i in range(2,n+1):
        c=[]
        c.append(a[i]+a[i-1])
        a=a+c
    return a[n]
        
#计算一个区间中的所有的1的个数，主要的处理思路是将数据转化成字符串处理
def getnums():
    n=int(input())
    nums=0
    for i in range(1,n+1):
        a=list(str(i))
        for i in range(len(a)):
            if(a[i]=='1'):
                nums+=1
    return nums

#计算出现次数为1的元素
a=[2,1,2,3,1]
b=[]
c=[]
def test(a):
    for i in range(len(a)):
        if a[i] not in b:
            b.append(a[i])
            c.append(0)
        for j in range(len(b)):
            if a[i]==b[j]:
                c[j]=c[j]+1
    for i in range(len(c)):
        if(c[i]%2==1):
            print(b[i])
    return b[i]

#计算出现次数为1的元素
def  test3(a):
    b=[]
    c=[]
    for i in range(len(a)):
        if a[i] not in b:
            b.append(a[i])
            c.append(0)
        for j in range(len(b)):
            if(a[i]==b[j]):
                c[j]=c[j]+1
    for i in range(len(c)):
        if(c[i]==max(c)):
            return b[i]
if __name__=="__main__":
    b=list(map(int,input().split(' ')))
    print(test3(b))
    
#计算斐波那契数列的简单的方法,输出最后一个数字
def fibonacci (n):
    a=[1,1,2]
    for i in range(2,n):
        a.append(a[i]+a[i-1])
    return a[-1]

#计算抽充好速度
    




#面试题58:翻转字符串
def ReverseSentence(sentence):
    res=sentence.split(' ')
    res.reverse()
    return ' '.join(res)
#面试58:左旋转字符串
def leftreverse(sentence,n):
    return sentence[n:len(sentence)]+sentence[0:2]
    


#计算第n个丑数

        
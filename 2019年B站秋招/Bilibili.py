# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:50:20 2019

@author: hello

"""
'''
22娘和33娘接到了小电视君的扭蛋任务：
一共有两台扭蛋机，编号分别为扭蛋机2号和扭蛋机3号，22娘使用扭蛋机2号，33娘使用扭蛋机3号。
扭蛋机都不需要投币，但有一项特殊能力：
扭蛋机2号：如果塞x（x范围为>=0正整数）个扭蛋进去，然后就可以扭到2x+1个
扭蛋机3号：如果塞x（x范围为>=0正整数）个扭蛋进去，然后就可以扭到2x+2个
22娘和33娘手中没有扭蛋，需要你帮她们设计一个方案，两人“轮流扭”（谁先开始不限，扭到的蛋可以交给对方使用），用“最少”的次数，使她们能够最后恰好扭到N个交给小电视君。

输入描述:

输入一个正整数，表示小电视君需要的N个扭蛋。

输出描述:

输出一个字符串，每个字符表示扭蛋机，字符只能包含"2"和"3"。

输入例子1:

10

输出例子1:

233
'''
'''
  思考,这个题目的基本思路是，首先确定给出的数据是奇数还是偶数，如果是奇数使用x=2x+1来
  计算，如果是偶数使用x=2x+2来计算，这是个基本的要求，然后迭代，直到最后的那个数据是0
  才中止这个计算，下面是简单的伪代码，
  设计空list c
  a为输入数据
  循环中止条件(a>0)
      如果a为偶数：
          c附上一个3
          a赋值为a/2-1
      否则：
          c附上一个2
          a复制为a/2-1/2
     
  将c逆序后转化成字符串
  
  格式化输入参数
  N=int(input())
  使用上面的函数处理后的数格式化输出
  
  下面是上面的算法的实现
  '''

x='1234'
y='34215'
print([i==j for i,j in zip(x,y)])
  
  
  
  
  
  
  
  
  
  
  
  
  
def test(a):
    c=[]
    while(a>0):
        if(a%2==0):
            c.append(3)  
            a=a/2-1
        else:
            c.append(2)
            a=a/2-1/2
    b=""
    c.reverse()
    for i in c:
        b=b+str(i)
    return b


def main():
    N=int(input())
    print(test(N))



'''


'''


a='misakamikotodaisuki'
 
 
def test1(n,a):
    b=list(a)
    c=[]
    d=[]
    for i in b:
        if(i not in c):
            c.append(i)
            d.append(0)
        
    for i in b:
        for j in range(len(c)):
            if(i==c[j]):
                d[j]=d[j]+1
    
    k=0
    l=-1
    for i in range(len(d)):
        if(d[i]==1):
            k=k+1
            l=i
        if(k==n):
            break

    if(l!=-1):
        result='['+c[l]+']'
    else:
        result='Myon~'
    return result
            

def main1(): 
    a=list(map(str,input().split(" ")))
    d=""
    for i in range(1,len(a)):
        d=d+a[i]
    result=test1(int(a[0]),d)
    print(result)
    


a=''
while(a!='END'):
    a=input()
    print(a)
    
  
    
import math
 
def test2(a):
    d=2*a[0]
    x1=a[1]
    y1=a[2]
    x2=a[3]
    y2=a[4]
    dist=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    num=round(dist/d)
    return num


a=list(map(int,input().split(" ")))
print(test2(a))
    








import math
 
def test2(a):
    d=2*a[0]
    x1=a[1]
    y1=a[2]
    x2=a[3]
    y2=a[4]
    dist=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    num=round(dist/d)
    return num

a=list(map(int,input().split(" ")))


print(test2(a))



import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))
    
    
    
    
N=int(input())
a=list(map(int,input().split(" ")))


def maxs(a):
    mas=0
    for i in a:
        if(i>mas):
            mas=i
    return mas

b=[1,2,4,6,7,8]
for j in range(1,len(b)):
    c=[]
    for i in range(len(b)-1):
        if(j==i):
            c.append(b[i+2]-b[i])
        else:
            c.append(b[i+1]-b[i])
    print(c)
    
    
    
    
    
    
def test(n,a):
    
    
    
n=int(input())
a=[]
for i in range(n-1):
    a.append(list(map(int,input().split(" "))))
    
    
    
    
    


def test2(m,n):
    
    
m=list(map(int,input().split(" ")))
n=list(map(int,input().split(" ")))






    
def test3(m,n):
    
    
m=list(map(int,input().split(" ")))
n=list(map(int,input().split(" ")))







def dfs(node):
    if node is None:
        return
    #建立空栈、建立空集合
    stack = []
    nodeSet = set()
    # 打印节点加入节点
    print(node.value)
    nodeSet.add(node)
    stack.append(node)
    while len(stack)>0:
        cur = stack.pop()  #弹出最近入栈的节点
        for next in cur.nexts: #遍历该节点的邻接节点
            if next not in nodeSet:
                # 把节点压入 邻接节点压入 登记节点 打印节点值 退出当前循环
                stack.append(cur)
                stack.append(next)
                nodeSet.add(next)
                print(next.value)
                break

node=[[1,2],[1,3],[3,4]]






def dfs(adj, start):
    visited = set()
    stack = [[start, 0]]
    while stack:
        (v, next_child_idx) = stack[-1]
        if (v not in adj) or (next_child_idx >= len(adj[v])):
            stack.pop()
            continue
        next_child = adj[v][next_child_idx]
        stack[-1][1] += 1
        if next_child in visited:
            continue
        print(next_child)
        visited.add(next_child)
        stack.append([next_child, 0])
 
 
graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
dfs(graph, 1)


def test(a):
    flag=True
    if(flag<0):
        flag=False
    else:
        c=list(str(a))
        for i in range(int(len(c)/2)):
            if(c[i]!=c[len(c)-i-1]):
               flag=False
               break
    return flag
           


nums = [-1, 0, 1, 2, -1, -4]
b=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(i+j+1,len(nums)):
            if(nums[i]+nums[j]+nums[k]==0):
                c=[]
                c.append(nums[i])
                c.append(nums[j])
                c.append(nums[k])
                print([i,j,k])
                print('数值')
                print(c)
                b.append(c)
        
        
        
        
a=input()
b=list(a)
if(b[0]=='-'):
    del b[0]
b.reverse()

i=0
while i<len(b):
    if(b[0]=='0'):
        del b[0]
    else:
        break
    
    
c="".join(b)

c=""
if(len(b)>0):
    for i in b:
        c=c+i

c=int(c)




    def reverse(x):
        b=list(str(x))
        if(b[0]=='-'):
            del b[0]
        b.reverse()
        i=0
        while i<len(b):
            if(b[0]=='0'):
                del b[0]
            else:
                break
        c=""
        if(len(b)>0):
            for i in b:
                c=c+i
  
        return int(c)

d=[]
for i in b:
    d.append(int(i))
    
    
sum=0
for i in range(len(d)):
    sum=sum+d[i]*pow(10,len(d)-i-1)
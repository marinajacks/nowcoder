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
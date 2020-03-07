class Solution {
        public static int searchInsert(int[] nums, int target) {
        int left=0,right=nums.length-1,index=(left+right)/2;
        if(target>nums[right]) {
        	index= right+1;
        }
        else if(target<nums[left]) {
        	index=0;
        }
        else {
        	while(left<=right){
        		if(nums[index]>target){
        			right=index-1;
        			index=(left+right)/2;
        			
        		}
        		else if(nums[index]<target){
        			left=index+1;
        			index=(left+right)/2;
        		}
        		else {
        			return index;
        		}
        	}	
		}        	
        return index+1;
	}
}

/*为了实现查找某个数据在数组中的位置，我们一般的处理思路显然是使用二分法。
在进行二分法进行分析之前，首先需要考虑的就是边界条件。
边界条件在于，假如target比有序数组的最大值大，那么返回这个数组的长度；
如果target比有序数组的最小值小，那么就返回0。
在考虑了边界值之后，接下来考虑的是使用二分法来判断一个数据在数组中的位置。
首先，设定两个地址信息，一个是左边的下标，一个是右边的坐标，在开始的时候，

查找一个数组元素的下标。

二分法适用于已经排好序的数组，定义两个变量，一个low,一个high,则mid=(low+high)/2
算法核心：

如果 value==arr[mid],中间值正好等于要查找的值，则返回下标，return mid;

如果 value<arr[mid],要找的值小于中间的值，则再往数组的小端找，high=mid-1;

如果 value>arr[mid],要找的值大于中间的值，则再往数组的大端找，low=mid+1;
根据上面的算法，可以得到对应的程序。






*/
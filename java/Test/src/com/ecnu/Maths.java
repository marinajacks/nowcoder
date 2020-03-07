package com.ecnu;

public class Maths {
	public static void main(String [] args) {
		int [] a= {1};
		System.out.println(searchInsert(a,1));
		
	}

	public static double sums(double[] nums) {
		double adds=0;
		for(int i=0;i<nums.length;i++) {
			adds+=nums[i];
		}
		return adds;
	}

	public static int searchInsert(int[] nums, int target) {
        int left=0,right=nums.length-1,index=(left+right)/2;
        System.out.println(left+"\t"+right+"\t"+index);
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
package com.ecnu;

public class Maths {
	public static void main(String [] args) {
		System.out.println("hello world!");
		double[] a= {21000,20000,181292,129207,155853,-120,-100};
		System.out.println(sums(a));
	}
	public static double sums(double[] nums) {
		double adds=0;
		for(int i=0;i<nums.length;i++) {
			adds+=nums[i];
		}
		return adds;
	}
}

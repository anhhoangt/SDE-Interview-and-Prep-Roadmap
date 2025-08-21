'''
Example 1: Given a string s, return true if it is a palindrome, false otherwise.

A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".

'''
def palindrom(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True
        

'''
125. Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true

Input: s = "race a car"
Output: false

Input: s = " "
Output: true
'''

def isPalindrome(s):
    s = ''.join(char for char in s if char.isalnum()).lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if (s[left] != s [right]):
            return False
        left += 1
        right -=1
    return True


'''
1. Two Sum - https://leetcode.com/problems/two-sum/description/ but SORTED

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]

'''
Example: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.
'''

def merged_sorted(arr1, arr2):
    i, j = 0, 0
    result = []
    while i < len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
            
    while i<len(arr1):
        result.append(arr1[i])
        i += 1
    
    while j<len(arr2):
        result.append(arr2[j])
        j += 1
    return result

print(merged_sorted([1,2,5,6], [4,5,7,8]))

'''
11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
'''
def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            high = min(height[left], height[right])
            maxArea = max(maxArea, width*high)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea



'''
LeetCode 186: Reverse Words in a String II.
Problem

You are given a character array s representing a string.

Words are separated by a single space.

You must reverse the order of the words in-place.
'''
    def reverseWords(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Helper: reverse a portion of the list in-place
        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        n = len(s)

        # Step 1: reverse the whole string
        reverse(0, n - 1)

        # Step 2: reverse each word individually
        start = 0
        for i in range(n + 1):  # +1 to handle the last word
            if i == n or s[i] == " ":  # word boundary
                reverse(start, i - 1)
                start = i + 1


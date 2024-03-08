class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums) 
        nums_1 = nums.copy()
        for i in range(length):
            j = (i + k) % length
            nums[j] = nums_1[i] 

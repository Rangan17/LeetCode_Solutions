class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i]= nums.count(i)
        List = list(freq.values())
        List.sort()
        i = List.count(max(List))
        j = i * max(List)
        return j


class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=2:
           return n
        bin_n=bin(n)[2:]
        return (2**len(bin_n))
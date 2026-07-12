class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank = {}
        
       
        sorted_arr = sorted(set(arr))
        
       
        for i, num in enumerate(sorted_arr):
            rank[num] = i + 1
        
       
        return [rank[num] for num in arr]
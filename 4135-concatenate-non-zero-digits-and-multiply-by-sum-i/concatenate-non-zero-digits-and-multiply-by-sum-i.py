class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = n
        rev = 0
        sum = 0
        while num > 0:
            mod = num % 10
            if mod > 0:
                rev = rev * 10 + mod
                sum += mod
            num /= 10
        
        rev = int(str(rev)[::-1])
        return rev * sum
        
        
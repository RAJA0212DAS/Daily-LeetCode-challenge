class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(s)
        b = bytearray(s.encode())  
        zero = ord('0')
        
        prefix_sum = [0] * (n + 1)
        prefix_val = [0] * (n + 1)
        prefix_count = [0] * (n + 1)
        pow10 = [1] * (n + 1)
        
        for i in range(n):
            d = b[i] - zero
            nz = d != 0
            prefix_count[i+1] = prefix_count[i] + nz
            prefix_sum[i+1] = prefix_sum[i] + (d if nz else 0)
            prefix_val[i+1] = (prefix_val[i] * 10 + d) % MOD if nz else prefix_val[i]
            pow10[i+1] = pow10[i] * 10 % MOD
        
        result = []
        append = result.append
        
        for l, r in queries:
            ds = prefix_sum[r+1] - prefix_sum[l]
            if ds == 0:
                append(0)
                continue
            count = prefix_count[r+1] - prefix_count[l]
            x = (prefix_val[r+1] - prefix_val[l] * pow10[count]) % MOD
            append(x * ds % MOD)
        
        return result
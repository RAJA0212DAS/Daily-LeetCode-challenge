class Solution(object):
    def gcdSum(self, nums):
        def prefixGcd(maximum,minimum):
            while minimum!=0:
                maximum,minimum=minimum,maximum%minimum
            return maximum
        r=[]
        m=0
        for i in nums:
            m=max(m,i)
            r.append(prefixGcd(i,m))
        r.sort()
        s=0
        for i in range(len(r)//2):
            s+=prefixGcd(r[i],r[len(r)-1-i])
        return s
class Solution(object):
    def minimumPushes(self, word):
        n=len(word)
        count=0
        i=1
        while n>0:
            if n>=8:
                count+=8*i
                i+=1
                n-=8
            else:
                count+=n*i
                n=0
                i+=1
        return count
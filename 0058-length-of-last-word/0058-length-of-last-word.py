class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        counter = 0
        i = 0
        n = len(s)
        while i<n:
            if s[-(i+1)] != ' ':
                counter += 1
                i+=1
            else:
                return counter
        return counter
        #return len(s.rsplit(maxsplit=1)[-1])

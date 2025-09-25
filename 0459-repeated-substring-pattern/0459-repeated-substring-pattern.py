def lps(s):
    """
    :type s: str
    :rtype: list
    Buiilds a lps table for provided string s
    """
    lps = [0]*len(s)
    lps[0] = 0
    j = 1
    val = 0
    while j < len(s):
        if s[j] == s[val]:
            val+=1
            lps[j] = val
            j+=1
        elif val!=0:
            val = lps[val-1]
        else:
            lps[j] = 0
            j+=1
    return lps
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        Building an lpm table, the last element index should be >= len/2
        """
        pattern = lps(s)[-1] - len(s)
        if len(s)%pattern == 0 and lps(s)[-1] !=0: return True
        return False
      


        

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_count = 1
        while char_count <= len(s)//2:
            sub_str = s[:char_count]
            res_str = "".join(s.split(sub_str))
            if len(res_str) == 0: return True
            char_count += 1
        return False

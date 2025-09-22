from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sMap = dict()
        tMap = dict()
        for char in s:
            sMap[char] = sMap.get(char, 0) + 1
        for char in t:
            tMap[char] = tMap.get(char, 0) + 1
        return tMap == sMap

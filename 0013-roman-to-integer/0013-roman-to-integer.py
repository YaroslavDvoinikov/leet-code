class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        string = "IVXLCDM"
        sum = 0
        i = 0
        while i < len(s):
            print(i)
            if s[i] in ('I','X','C') and i!=len(s)-1:
                if s[i+1] == string[(string.index(s[i]))+1] or s[i+1] == string[(string.index(s[i]))+2]: # if the next element of the given string next or 2 steps next in roman hierarchy,
                    # we will substitute value of s[i] from s[i+1], e.g. IV = 5-1 pr IX = 10 -1, string(string.index(s[i]+1)) is used to understand which element we should look up e.g I -> V; X ->L
                    sum+= (roman[s[i+1]]-roman[s[i]])
                    i+=2
                    continue
            sum += roman[s[i]]
            i+=1
        return sum

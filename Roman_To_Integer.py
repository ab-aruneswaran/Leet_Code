class Solution:
    def romanToInt(self, s: str) -> int:
        i=0
        res=0
        def value(R):
            if (R == 'I'):
                return 1
            if (R == 'V'):
                return 5
            if (R == 'X'):
                return 10
            if (R == 'L'):
                return 50
            if (R == 'C'):
                return 100
            if (R == 'D'):
                return 500
            if (R == 'M'):
                return 1000

        while (i < len(s)):
            s1 = value(s[i])
            if (i+1 < len(s)):
                s2 = value(s[i+1])
                if (s1>=s2):
                    res=res+s1
                    i=i+1
                else:
                    res=res+s2-s1
                    i=i+2
            else:
                res=res+s1
                i=i+1
        return res

    

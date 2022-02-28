"""
Input: s = "III"
Output: 3
Explanation: III = 3.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

def romantoint(s:str) -> int:
    d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    res = 0
    for i in range(0, len(s)-1):
        if d[s[i]] < d[s[i+1]]:
            res -= d[s[i]]
        else:
            res += d[s[i]]
    return res + d[s[-1]]
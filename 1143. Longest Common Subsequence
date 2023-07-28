class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prevrow = [0] * (len(text2)+1)
        for i in range(len(text1)-1,-1,-1):
            currow = [0]* (len(text2)+1)
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    currow[j] = 1 + prevrow[j+1]
                else:
                    currow[j] = max(currow[j+1],prevrow[j])
            prevrow = currow
        return prevrow[0]


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curLen = 1
        maxLen = 1
        prev = ''

        for i in range(1, len(arr)):
            if arr[i-1] > arr[i] and prev != '>':
                curLen = curLen+1
                prev = '>'
            elif arr[i-1] < arr[i] and prev != '<':
                curLen = curLen+1
                prev = '<'
            else:
                if arr[i-1] == arr[i]:
                    prev = ''
                    curLen = 1
                elif arr[i-1] > arr[i]:
                    prev = '>'
                    curLen = 2
                else:
                    prev = '<'
                    curLen = 2
            maxLen = max(curLen, maxLen)
        return maxLen

# using kadane's or sliding algorithm
# consider edge case for 8=8

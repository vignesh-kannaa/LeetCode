"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # solution 1: using maxHeap, O(k logn)
        # d = {}
        # maxHeap = []
        # res = []
        # for n in nums:
        #     d[n] = 1 + d.get(n,0)
        # for key,value in d.items():
        #     heapq.heappush(maxHeap,[-value,key])
        # for _ in range(k):
        #     c,i = heapq.heappop(maxHeap)
        #     res.append(i)
        # return res

        # solution 2: using reverse BucketSort , O(n)
        d = {}
        freq = [[] for i in range(len(nums)+1)]  # list of list
        res = []
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        for key, value in d.items():
            freq[value].append(key)
        for i in range(len(freq)-1, 0, -1):
            for l in freq[i]:
                res.append(l)
                if len(res) == k:
                    return res


"""hashmap + 
sol1: maxheap 
sol2: reverse bucket sort. ie) use count as index and list of input as values"""

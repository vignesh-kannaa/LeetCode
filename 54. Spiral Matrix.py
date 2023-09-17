"""Given an m x n matrix, return all elements of the matrix in spiral order.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        L, R = 0, len(matrix[0])-1
        T, B = 0, len(matrix)-1
        res = []
        while L <= R and T <= B:
            for i in range(L, R+1):
                res.append(matrix[T][i])
            T += 1
            for i in range(T, B+1):
                res.append(matrix[i][R])
            R -= 1
            # edge case
            if not (L <= R and T <= B):
                break
            for i in range(R, L-1, -1):
                res.append(matrix[B][i])
            B -= 1
            for i in range(B, T-1, -1):
                res.append(matrix[i][L])
            L += 1
        return res

        """4 pointers L, R, T, B
        after iterating one section increment/decrement them
        check edge case 1*3 or 3*1 matrix in between"""

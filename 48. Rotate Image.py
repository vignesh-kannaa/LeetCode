"""You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        L, R = 0, len(matrix[0])-1
        while L < R:
            for i in range(R-L):  # for inner loop count is reduced from both L and R
                T, B = L, R
                TopLeft = matrix[T][L+i]
                matrix[T][L+i] = matrix[B-i][L]
                matrix[B-i][L] = matrix[B][R-i]
                matrix[B][R-i] = matrix[T+i][R]
                matrix[T+i][R] = TopLeft
            R -= 1
            L += 1


"""SOL:
use 4 pointers L, R, T, B
save Topleft in temp and rotate in reverse
while loop => layer
for loop => next elem"""

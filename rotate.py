class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Rotating is the reverse columns tranpose
        matrix[:] = zip(*matrix[::-1])

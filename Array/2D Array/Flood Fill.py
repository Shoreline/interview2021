class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:  # corner case
            return image

        def helper(x, y):
            if 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == original_color:
                image[x][y] = color
                helper(x + 1, y)
                helper(x - 1, y)
                helper(x, y + 1)
                helper(x, y - 1)

        helper(sr, sc)
        return image
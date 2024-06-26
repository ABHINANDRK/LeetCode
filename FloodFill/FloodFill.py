    
#     You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

 

# Example 1:


# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
# Example
from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if(image[sr][sc] == color or image == None):
        return image

    fill(image,sr,sc,image[sr][sc],color)
    return image


def fill(image: List[List[int]], sr: int, sc: int, initial: int, newColor: int) -> List[List[int]]:
    if(sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != initial):
        return

    image[sr][sc] = newColor

    fill(image,sr,sc + 1,initial,newColor)
    fill(image,sr,sc - 1,initial,newColor)
    fill(image,sr + 1,sc - 1,initial,newColor)
    fill(image,sr - 1,sc,initial,newColor)


if __name__ == '__main__':
    print(floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
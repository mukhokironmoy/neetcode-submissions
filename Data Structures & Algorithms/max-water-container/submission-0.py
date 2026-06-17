class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1

        max_area = [0,None,None] # A list that will store area, start and end

        while start < end:
            # The length of container will be min of both bars as beyond that it will spill
            length = min(heights[start], heights[end])

            # The width is the distance btw the two bars
            width = end - start

            area = length * width

            if area > max_area[0]:
                max_area[0] = area
                max_area[1] = start
                max_area[2] = end

            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return max_area[0]

            
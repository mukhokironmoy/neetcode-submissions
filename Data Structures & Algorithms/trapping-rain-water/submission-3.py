class Solution:
    def trap(self, height: List[int]) -> int:

        # Store values for tallest building to the left
        left = [0] * len(height)

        for i in range(1, len(height)): # We ignore the first index as there are no buildings to the left of it
            height_of_immediate_left = height[i-1]

            if height_of_immediate_left > left[i-1]:
                left[i] = height_of_immediate_left
            else:
                left[i] = left[i-1]

        
        # Store values for tallest building to the right
        right = [0] * len(height)
        right_most = len(height) - 1
        for i in range(right_most-1, -1, -1): # We ignore the last index as there are no buildings to the right of it
            height_of_immediate_right = height[i+1]

            if height_of_immediate_right > right[i+1]:
                right[i] = height_of_immediate_right
            else:
                right[i] = right[i+1]

        total_water = 0

        for i in range(len(height)):
            tallest_on_left = left[i]
            tallest_on_right = right[i]

            max_height_of_water = min(tallest_on_left, tallest_on_right) # Because water would spill out of the shorter building, so water will be at most till shortest height

            height_occupied_by_building = height[i]

            net_water_at_i = max_height_of_water - height_occupied_by_building

            if net_water_at_i >= 0:
                total_water += net_water_at_i
        
        print(height)
        print(left)
        print(right)
        return total_water

        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_indices = []

        for i in range(len(nums)):
            nums_with_indices.append((nums[i], i))

        # Sort the new list
        nums_with_indices.sort(key = lambda x: x[0])

        start = 0
        end = len(nums)-1

        while start < end:
            if nums_with_indices[start][0] + nums_with_indices[end][0] > target:
                end -= 1
            elif nums_with_indices[start][0] + nums_with_indices[end][0] < target:
                start += 1
            elif nums_with_indices[start][0] + nums_with_indices[end][0] == target:
                lower = min(nums_with_indices[start][1], nums_with_indices[end][1])
                upper = max(nums_with_indices[start][1], nums_with_indices[end][1])
                return [lower, upper]


        # seen = dict({})

        # for i in range(len(nums)):
        #     if target - nums[i] in seen:
        #         return [seen[target - nums[i]], i]
        #     seen[nums[i]] = i      
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            # If the sum is greater than target then every sum using numbers ahead of start would also be greater than target. Hence reduce the end.
            if numbers[start] + numbers[end] > target:
                end -= 1
            
            # If the sum is lesser than target then every sum using numbers before start would also be lesser than target. Hence increase the start
            elif numbers[start] + numbers[end] < target:
                start += 1

            elif numbers[start] + numbers[end] == target:
                return [start+1,end+1]
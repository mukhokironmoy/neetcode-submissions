class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_counts = dict()
        prefix_sum_counts[0] = 1

        current_sum = 0
        valid_subarrays = 0

        for num in nums:
            current_sum += num

            needed = current_sum - k

            if needed in prefix_sum_counts:
                valid_subarrays += prefix_sum_counts[needed]

            prefix_sum_counts[current_sum] = prefix_sum_counts.get(current_sum, 0) + 1

        return valid_subarrays
        
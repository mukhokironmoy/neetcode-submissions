class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        explored = dict({})
        longest_len = 0

        for num in nums:
            explored[num] = False


        for i in range(len(nums)):
            num = nums[i]
            cur_len = 1

            next_num = num+1
            while next_num in explored and explored[next_num] == False:
                cur_len += 1
                next_num+=1

            prev_num = num-1
            while prev_num in explored and explored[prev_num] == False:
                cur_len += 1
                prev_num -= 1

            if cur_len > longest_len:
                longest_len = cur_len

        return longest_len
                

            
        
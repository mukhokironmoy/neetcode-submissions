class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
            
        nums.sort()
        seqs = []
        cur_seq = [nums[0]]

        for i in range(len(nums)):
            num = nums[i]

            if num == cur_seq[-1]:
                continue

            elif num == cur_seq[-1] + 1:
                cur_seq.append(num)

            else:
                seqs.append(cur_seq)
                cur_seq = [num]

        seqs.append(cur_seq)

        longest_seq = 0
        for seq in seqs:
            if len(seq) > longest_seq:
                longest_seq = len(seq)

        return longest_seq

        # # Initialise a dict that keeps track of whether we have seen a no or not
        # explored = dict({})
        # for num in nums:
        #     explored[num] = False
        
        # # Initialise a counter that tracks the longest len
        # longest_len = 0

        # # For each num in the list
        # for i in range(len(nums)):
        #     num = nums[i]

        #     # Start a seq with this num
        #     cur_len = 1

        #     # Start checking if a consecutive chain can be formed ahead of it
        #     next_num = num+1
        #     while next_num in explored and explored[next_num] == False: # only look ahead if the numbers are in +1 order and if we have not tracked it
        #         explored[next_num] = True
        #         cur_len += 1 # increase the len of the chain if we find such no
        #         next_num+=1

        #     # Start checking if a consecutive chain can be formed behind it
        #     prev_num = num-1
        #     while prev_num in explored and explored[prev_num] == False: # only look ahead if the numbers are in +1 order and if we have not tracked it
        #         explored[next_num] = True                
        #         cur_len += 1 # increase the len of the chain if we find such no
        #         prev_num -= 1

        #     if cur_len > longest_len:
        #         longest_len = cur_len

        # return longest_len
                

            
        
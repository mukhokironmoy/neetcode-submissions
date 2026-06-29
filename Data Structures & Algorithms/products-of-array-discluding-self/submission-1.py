class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left prod
        left_prod = [1]*(len(nums)+1)

        for i in range(1,len(nums)):
            left_prod[i] = left_prod[i-1] * nums[i-1]

        # right prod
        right_prod = [1]*(len(nums)+1)

        for i in range(len(nums)-2, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i+1]

        
        print(left_prod)
        print(right_prod)

        prod = [1]*len(nums)

        for i in range(len(prod)):
            prod[i] = left_prod[i] * right_prod[i]

        return prod


        # prefix_mul = [1]*(len(nums))
        # suffix_mul = [1]*(len(nums))
        # nums_rev = nums[-1::-1]
        # # print(nums_rev)

        # for i in range(1,len(nums)):
        #     prefix_mul[i] = prefix_mul[i-1] * nums[i-1]
        #     suffix_mul[i] = suffix_mul[i-1] * nums_rev[i-1]

        # suffix_mul = suffix_mul[-1::-1]

        # print(prefix_mul)
        # print(suffix_mul)
        # prod = []

        # for i in range(len(nums)):
        #     prod.append(prefix_mul[i] * suffix_mul[i])

        # return prod

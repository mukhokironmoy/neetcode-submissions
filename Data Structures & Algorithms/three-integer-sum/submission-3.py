class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the list
        nums.sort()
        # print(nums)

        # Initialise the result
        triplets = []

        # Run a loop to fix t1
        for i in range(len(nums)-2):

            # Skip any iterations where t1 is repeated as we want unique triplets
            if i>0 and nums[i] == nums[i-1]:
                continue

            t1 = nums[i]
            # print(f"t1: {t1}")
            start = i+1
            end = len(nums)-1

            while start < end:
                t2 = nums[start]
                t3 = nums[end]
                # print(f"t2: {t2} t3: {t3}")

                if t1+t2+t3 > 0: # If the sum > 0, that means end digit is too big for this triplet sum
                    end -= 1

                elif t1+t2+t3 < 0: # If the sum < 0, that means the start digit is too small for this triplet sum
                    start += 1

                elif t1+t2+t3 == 0:
                    triplet = [t1,t2,t3]
                    triplets.append(triplet)

                    start += 1
                    end -= 1

                    # Now we skip any iterations where t2 or t3 are repeated as question asks for unique triplets
                    while start < end and nums[start] == nums[start-1]:
                        start += 1

                    while start < end and nums[end] == nums[end+1]:
                        end -= 1

        
        return triplets


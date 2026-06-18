class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Initialise the target signature
        target=[0]*26
        for i in range(len(s1)):
            index = ord(s1[i]) - ord('a')
            target[index] += 1
        
        # Initialise the window signature
        window = [0]*26
        for i in range(len(s1)):
            index = ord(s2[i]) - ord('a')
            window[index] += 1

        left = 0
        right = len(s1)-1
        print(left, right)

        if window == target:
            return True


        for i in range(1, len(s2)-len(s1)+1):
            # Move the left index ahead by 1
            left_idx = ord(s2[left]) - ord('a')
            window[left_idx] -= 1
            left += 1

            # Move the right index ahead by 1
            right += 1
            right_idx = ord(s2[right]) - ord('a')
            window[right_idx] += 1

            print(left,right)
            if window == target:
                return True            


        return False



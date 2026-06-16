class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""

        for c in s:
            if c.isalnum():
                s1 = s1 + c.lower()

        print(s1)

        # For 5(odd) go till i=2, For 6(even) go till i=3
        n = len(s1)//2
        print(n)


        for i in range(n):
            if s1[i] == s1[len(s1)-i-1]:
                continue
            else:
                return False

        return True

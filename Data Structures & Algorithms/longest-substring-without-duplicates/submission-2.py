class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        seen = set()
        start = 0
        end = 1
        
        seen.add(s[start])
        longest_substring = [1, start, start]

        while end < len(s):
            if s[end] in seen:
                
                while s[end] in seen: # Move start forward till the new char can fit
                    seen.remove(s[start])
                    start += 1

            
            seen.add(s[end])

            if end-start+1 > longest_substring[0]:
                longest_substring[0] = end-start+1
                longest_substring[1] = start
                longest_substring[2] = end

            end += 1

        return longest_substring[0]



        # if len(s) == 0:
        #     return 0
        # elif len(s) == 1:
        #     return 1

        # start = 0
        # end = 0
        # seen = set()
        # seen.add(s[start])

        # longest_substr = [0,start,end]


        # while end < len(s):

        #     # For the first element
        #     if start == end:
        #         pass

        #     # If we run into a repeated char
        #     elif s[end] in seen:
                
        #         while s[end] in seen:   # Move start ahead till the set no longer has that element
        #             seen.remove(s[start])
        #             start+=1

        #         seen.add(s[end])

        #     # If it is not a repeated char, track and move on
        #     else:
        #         seen.add(s[end])

        #     cur_substr_len = end - start + 1
        #     if cur_substr_len > longest_substr[0]:
        #         longest_substr[0] = cur_substr_len
        #         longest_substr[1] = start
        #         longest_substr[2] = end
                
        #     end += 1

        # return longest_substr[0]

                
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Logic :
        """"
            Create a window
            Keep track of the freq of all the elements in the window

            note 1 - we are only allowed to make k changes to the window
            note 2 - we need to find the window where if we make k changes, we get the longest repeating characters

            For each window, we would not want to change char that are most repeating
            So changeable_char = window_size - max_freq_of_chars

            If the no of chars we can change > k, shrink the window
        """

        start = 0
        end = 0

        char_freq_in_window = dict()
        max_freq_in_window = 0

        max_window_size = 0

        while end < len(s):
            # Update the freq of the new element
            char_freq_in_window[s[end]] = char_freq_in_window.get(s[end], 0) + 1
            if char_freq_in_window[s[end]] > max_freq_in_window:
                max_freq_in_window = char_freq_in_window[s[end]]

            cur_window_size = end - start + 1

            # No of chars we can change is total - freq of max char
            changeable_chars = cur_window_size - max_freq_in_window

            while changeable_chars > k:
                char_freq_in_window[s[start]] -= 1
                start+=1 # Shrink the window

                # Recalculate values
                max_freq_in_window = max(char_freq_in_window.values()) 
                cur_window_size -= 1
                changeable_chars = cur_window_size - max_freq_in_window

            if cur_window_size > max_window_size:
                max_window_size = cur_window_size

            end += 1
        return max_window_size
            

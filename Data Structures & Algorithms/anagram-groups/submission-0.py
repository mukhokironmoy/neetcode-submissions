class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict({})

        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in anagrams:
                group = anagrams[sorted_string]
                group.append(string)
                anagrams[sorted_string] = group
            else:
                anagrams[sorted_string] = [string]

        return list(anagrams.values())

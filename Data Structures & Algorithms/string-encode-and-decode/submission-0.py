class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""

        for string in strs:
            n = len(string)
            out = out + f"{n}#{string}"

        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i=0
        word_len = ""

        while i < len(s):
            if s[i]=='#':
                word_len = int(word_len)
                i+=1
                word = ""

                for j in range(word_len):
                    word = word + s[i]
                    i+=1

                out.append(word)
                word_len = ""

                if i==len(s):
                    break

            word_len = word_len + s[i]
            i+=1

        return out
                
                

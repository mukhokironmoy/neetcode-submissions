class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        mon_stack = []

        for i in range(len(temperatures)-1, -1, -1):
            
            if not mon_stack: # If the stack is empty -> No temp warmer, hence 0
                mon_stack.append(i)
                continue

            else:
                # Remove temps that are lower than current
                while mon_stack and temperatures[mon_stack[-1]] <= temperatures[i]:
                    mon_stack.pop()

                if mon_stack:
                    result[i] = mon_stack[-1] - i
                else:
                    pass

                mon_stack.append(i)

        
        return result

            
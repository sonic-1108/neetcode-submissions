class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack:
                j = stack[-1]

                if temperatures[i] > temperatures[j]:
                    result[j] = i - j
                    stack.pop()
                else:
                    break

            stack.append(i)

        return result

            
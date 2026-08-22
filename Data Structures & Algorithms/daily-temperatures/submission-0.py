class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [];
        temp_len = len(temperatures)
        result = [0] * temp_len

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # if curr temp > last temp, update result
                stackTemp, stackIdx = stack.pop()
                result[stackIdx] = i - stackIdx # the distance betw the curr vs all prev smaller stackIdx
            stack.append((t, i))

        return result



        
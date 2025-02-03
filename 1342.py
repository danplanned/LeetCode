class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        temp = num
        while (temp != 0):
            if(temp % 2 == 0):
                temp = temp/2
            else:
                temp = temp-1
            steps += 1
        print(steps)
        return steps

sol = Solution()
sol.numberOfSteps(14)





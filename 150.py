class Solution:
    def evalRPN(self, nums: List[str]) -> int:
        stack = []
        ops = ['+','-','/','*']

        for i in range(0,len(nums)):
            if nums[i] not in ops:
                stack.append(nums[i])
            else:
                if stack:
                    pop1 = int(stack.pop())
                    pop2 = int(stack.pop())
                    if nums[i] == '+':
                        res = pop1 + pop2
                    elif nums[i] == '-':
                        res = pop2 - pop1
                    elif nums[i] == '*':
                        res = pop2 * pop1
                    else:
                        res = int(pop2 / pop1)
                    stack.append(res)
        return int(stack[0])
        

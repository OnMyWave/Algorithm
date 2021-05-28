class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        answer = 0 
        for block in enumerate(height):
            try:
                if block[1] != 0:
                    if stack[-1][1] <= block[1]:
                        pop_component = stack.pop()
                        black = 0
                        for k in range(pop_component[0]+1,block[0]):
                            black += height[k]
                        answer += (pop_component[1]*(block[0]-pop_component[0]-1) - black)
                        stack.append(block)
                    else: 
                        stack.append(block)

            except:
                stack.append(block)
                # print(answer)

        return answer

wave = Solution()
wave.trap([0,1,0,2,1,0,1,3,2,1,2,1])
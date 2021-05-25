class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        x_front = [s for s in x]
        x_back = [s for s in x[::-1]]

        # 정방향이랑 역방향이 처음부터 끝까지 같으면 Palindrome
        for i,j in zip(x_front,x_back):
            if i != j :
                return False
        
        # 반복문을 빠져나오면 True값 반환
        return True
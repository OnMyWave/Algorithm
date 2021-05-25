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

    # 위에서 주저리 주저리 써놨던 구조를 pop으로 단순하게 해결 가능
    def isPalindromeVersion2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = [char for char in str(x)]

        # Pop
        while len(x):
            if x.pop() != x.pop(0):
                return False
        
        # 반복문을 빠져나오면 True값 반환
        return True

    # pop을 이용하는 것은 같지만 list가 아니라 효율성이 좋은 deque 이용
    def isPalindromeVersion3(self, x):
        """
        :type x: int
        :rtype: bool
        """
        from collections import deque

        x = deque([char for char in str(x)])

        # Pop
        while len(x):
            if x.pop() != x.popleft():
                return False
        
        # 반복문을 빠져나오면 True값 반환
        return True

    def isPalindromeVersion4(self, x):
        """
        :type x: int
        :rtype: bool
        """
        from collections import deque

        x = deque([char for char in str(x)])

        # Pop
        while len(x):
            if x.pop() != x.popleft():
                return False
        
        # 반복문을 빠져나오면 True값 반환
        return True
    
    def isPalindromeVersion5(self, x):
        """
        :type x: int
        :rtype: bool
        """
        import re

        x = str(x).lower()
        x = re.sub('[^a-z0-9','',x)

        return x == x[::-1]

    
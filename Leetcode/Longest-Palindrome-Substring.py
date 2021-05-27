class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = []
        length = len(s)
        if len(s) < 2 :
            return s
        
        for i in range(length):
            current_idx_str = list()
            for j in range(min(i+1,length-i-1)):
                if s[i-j] == s[i+j+1]:
                    current_idx_str += s[i-j:i+j+2]
                    print(current_idx_str) 
                else:
                    break
            answer.append(current_idx_str)
            
        answer.sort(reverse=True,key=len)
            
        
        return answer

a = Solution()
print(a.longestPalindrome("babad"))
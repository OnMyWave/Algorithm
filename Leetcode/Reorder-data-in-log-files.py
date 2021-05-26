class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        log_list = [[l for l in log.split()] for log in logs]
        
        letter_log_list = []
        digit_log_list = []
        
        # letter group or digit group으로 나누기
        for log in log_list:
            if log[1].isalpha():
                letter_log_list.append(log)
            else:
                digit_log_list.append(log)

        # lambda 함수를 통해 정렬
        letter_log_list = sorted(letter_log_list, key = lambda x : (x[1:],x[0]))
        
        answer = []
        for letter in letter_log_list:
            answer.append(' '.join(letter))
        for digit in digit_log_list:
            answer.append(' '.join(digit))
        return answer
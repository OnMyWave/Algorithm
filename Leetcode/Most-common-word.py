class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re
        from collections import Counter
        
        p = re.sub(r"[!?',;.]",' ',paragraph)
        while '  ' in p:
            p = p.replace('  ',' ')
            
        if p[-1] == ' ':
            p = p[:-1]
            
        p = p.lower()
        cnter = Counter(p.split())
        cnter = sorted(cnter.items(), key = lambda x:(-x[1],x[0]))


        for item in cnter:
            if item[0] not in banned:
                return item[0]
from typing import get_args


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from itertools import permutations
        answer = []
        # for word in strs:
        while strs:
            str_list = []
            str_list.append(strs[0])
            comb_list = list(permutations([s for s in strs.pop(0)],len(str_list[0])))
            
            for comb in comb_list:
                joined_str = "".join(comb)
                while joined_str in strs:
                    str_list.append(joined_str)
                    strs.remove(joined_str)

            answer.append(str_list)

        return answer


    def groupAnagrams2(self, strs):
        from collections import defaultdict
        dic = defaultdict(list)
        for s in strs:
            word = ''.join(sorted(s))
            dic[word].append(s)
        
        return dic.values()

a = Solution()
print(a.groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))
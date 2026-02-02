# 14. Longest Common Prefix

from typing import List


class LongestCommonPrefix:
    def test_case(self):
        print(__name__)
        self.longestCommonPrefix(["flower","flow","flight"])
        self.longestCommonPrefix(["dog","racecar","car"])
        return

    def longestCommonPrefix(self, strs: List[str]) -> str:
        print('----- longestCommonPrefix start -----', strs)
        result = strs[0]
        for str in strs[1:]:
            result = self.search_prefix(result, str)
            if result == "":
                break
        print('result:', result)
        return result
    

    def search_prefix(self, prefix, compared):
        print('prefix:', prefix, 'compared:', compared)
        result = ""
        length = len(prefix) if len(prefix) < len(compared) else len(compared)
        for index in range(length):
            if prefix[index] == compared[index]:
                result += prefix[index]
            else:
                break
        return result

# 28. Find the Index of the First Occurrence in a String
# TODO: next time, use the KMP Algorithm

class FindIndexOfFirstOccurrenceInString:
    def test_case(self):
        print(__name__)
        self.strStr("sadbutsad", "sad")
        self.strStr("leetcode", "leeto")
        return

    def strStr(self, haystack: str, needle: str) -> int:
        print('----- start -----', haystack, needle)
        result = haystack.find(needle)
        print('result', result)
        return result
    
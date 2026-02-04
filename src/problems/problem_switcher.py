from problems import *

def execute(Problem_num):
    match Problem_num:
        case "13": RomanToInteger().test_case()
        case "14": LongestCommonPrefix().test_case()
        case "20": ValidParentheses().test_case()
        case "21": MergeTwoSortedLists().test_case()
        case "26": RemoveDuplicatesfromSortedArray().test_case()
        case _: print(f"The problem #{Problem_num} doesn't exist.")
    pass
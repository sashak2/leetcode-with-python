# import problems.easy as ps
from problems import *

def execute(Problem_num):
    match Problem_num:
        case "13": RomanToInteger().test_case()
        case "14": LongestCommonPrefix().test_case()
        case "20": ValidParentheses().test_case()
        case _: print(f"The problem #{Problem_num} doesn't exist.")
    pass
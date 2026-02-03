# 20. Valid Parentheses

class ValidParentheses:
    parentheses = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    def test_case(self):
        print(__name__)
        self.isValid("()")
        self.isValid("()[]/{/}")
        self.isValid("(]")
        self.isValid("([])")
        self.isValid("([)]")
        return

    def isValid(self, s: str) -> bool:
        print('----- start -----', s)
        result = True
        print('----- end result -----', result)
        return result

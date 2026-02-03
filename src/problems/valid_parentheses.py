# 20. Valid Parentheses

class ValidParentheses:
    parentheses = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    def test_case(self):
        print(__name__)
        self.isValid("()")
        self.isValid("()[]{}")
        self.isValid("(]")
        self.isValid("([])")
        self.isValid("([)]")
        self.isValid("[")
        self.isValid("((")
        self.isValid("]")
        return

    def isValid(self, s: str) -> bool:
        print('----- start -----', s)
        result = True
        stack = []
        for char in s:
            if char in self.parentheses:
                if len(stack) == 0 or self.parentheses[char] != stack.pop():
                    result = False
                    break
            else:
                stack.append(char)
        if len(stack) > 0:
            result = False
        print('result', result)
        return result

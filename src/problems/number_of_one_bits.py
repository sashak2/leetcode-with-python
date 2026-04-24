# 191. Number of 1 Bits

class NumberOfOneBits:
    def test_case(self):
        print(__name__)
        self.execute(11)
        self.execute(128)
        self.execute(2147483645)
        return

    def execute(self, n: int) -> int:
        print('----- start -----', n)
        result = 0
        while n > 0:
            if n & 1:
                result += 1
            n = n >> 1
        print('result', result)
        return result
    
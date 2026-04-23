# 190. Reverse Bits

class ReverseBits:
    def test_case(self):
        print(__name__)
        self.execute(43261596)
        self.execute(2147483644)
        return

    def execute(self, n: int) -> int:
        print('----- start -----', n)
        binary_str = f"{n:032b}"
        reversed_binary_str = binary_str[::-1]
        result = int(reversed_binary_str, 2)
        print('result', result)
        return result
    
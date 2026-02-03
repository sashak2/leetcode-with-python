# 13. Roman to Integer

class RomanToInteger:
    dict_roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def test_case(self):
        self.romanToInt("III")      # 3 = III(3)
        self.romanToInt("LVIII")    # 58 = L(50) + V(5) + III(3)
        self.romanToInt("MCMXCIV")  # 1994 = M(1000) + CM(900) + XC(90) + IV(4)
        # self.romanToInt("IV")
        # self.romanToInt("IX")
        # self.romanToInt("XL")
        # self.romanToInt("XC")
        # self.romanToInt("CD")
        # self.romanToInt("CM")
        return

    def romanToInt(self, s: str) -> int:
        # print('----- romanToInt start -----', s)
        result = self.dict_roman[s[-1]]
        previous_num = result
        for romain_num in s[-2::-1]:
            current_num = self.dict_roman[romain_num]
            # print('previous_num:', previous_num, 'current_num:', current_num)
            if current_num < previous_num:
                result -= current_num
            else:
                result += current_num                
            previous_num = current_num
        print('result:', result)
        return result

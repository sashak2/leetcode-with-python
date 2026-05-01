# 70. Climbing Stairs

# 4 -> 5 steps
# 1 1 1 1
# 1 1 2
# 1 2 1 
# 2 1 1 
# 2 2

# 5 -> 8 steps
# 1 1 1 1 1
# 1 1 1 2
# 1 1 2 1
# 1 2 1 1
# 2 1 1 1
# 1 2 2
# 2 1 2
# 2 2 1

# 6 ->  13 steps
# 1 1 1 1 1 1
# 1 1 1 1 2
# 1 1 1 2 1
# 1 1 2 1 1
# 1 2 1 1 1
# 2 1 1 1 1
# 1 1 2 2
# 1 2 1 2
# 2 1 1 2
# 2 1 2 1
# 2 2 1 1
# 1 2 2 1
# 2 2 2



class ClimbStairs:
    def test_case(self):
        print(__name__)
        self.execute(2)
        self.execute(3)
        return

    def execute(self, n: int) -> int:
        print('----- start -----', n)
        result = 0
        print('result', result)
        return result
    
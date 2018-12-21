class Solution_once:
    def singleNumber(self, arr):
        one, two = 0, 0
        for Y in arr:
            one, two = (one ^ Y) & ~two, (one & Y) | (two & ~Y)
        assert two == 0
        return one
class Solution_twice:
    def single_number(arr):
        one, two, threes = 0, 0, 0
        for Y in arr:
            one, two, threes = (~Y & one) | (Y & ~one & ~two & ~threes), (~Y & two) | (Y & one), (~Y & threes) | (Y & two)
        return two

if __name__ == "__main__":
    print(Solution_once().singleNumber([1, 1, 1, 2, 2, 2, 3]))
    print(Solution_once().singleNumber([5, 3, 0, 3, 5, 5, 3]))

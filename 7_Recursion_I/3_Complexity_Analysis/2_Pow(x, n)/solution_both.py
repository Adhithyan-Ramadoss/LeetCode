class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n == 0:
            return 1

        if n % 2:
            return x * self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2)
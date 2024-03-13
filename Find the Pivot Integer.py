class Solution:
    def pivotInteger(self, n: int) -> int:
        sum =0
        for i in range(n+1):
            sum += i
        x = math.sqrt(sum)
        if x.is_integer():
            return int(x)
        else:
            return -1

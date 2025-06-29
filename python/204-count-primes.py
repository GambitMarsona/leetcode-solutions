class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        vals = [True]*n
        vals[0], vals[1] = False, False
        limit = n**0.5
        counter = 2
        while counter < limit:
            if vals[counter]:
                for num in range(2*counter,n,counter):
                    vals[num] = False 
            counter += 1
        return sum(vals)

        
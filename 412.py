class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # ret = []
        # for i in range(n):
        #     if (i+1) % 3 == 0:
        #         if (i+1) % 5 ==0:
        #             ret.append("FizzBuzz")
        #         else:
        #             ret.append("Fizz")
        #     elif (i+1) % 5 == 0:
        #         ret.append("Buzz")
        #     else:
        #         ret.append(str(i+1))

        # return ret        

        ret = [str(i+1) for i in range(n)]

        for i in range(2,n,3):
            ret[i] = "Fizz"

        for i in range(4,n,5):
            ret[i] = "Buzz"
        
        for i in range(14,n,15):
            ret[i] = "FizzBuzz"
        
        return ret

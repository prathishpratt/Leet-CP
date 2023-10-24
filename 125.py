def isPalindrome(self, s: str) -> bool:
        
        k= ""
        for i in s:
            if i.isalnum():
                k=k+i
        k=k.lower()
        return k==k[::-1]
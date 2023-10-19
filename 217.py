def containsDuplicate(self, nums: List[int]) -> bool:
        has = {}
        for i in range(0,len(nums)):
            if nums[i] in has.keys():
                return True
            else:
                has[nums[i]] = 1
        return False
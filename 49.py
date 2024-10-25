class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #SOL 1 - HITS TLE
        # has = [[strs[0]]]

        # for i in strs[1:]:
        #     flag = 0
        #     for j in has:
        #         if sorted(i) == sorted(j[0]):
        #             j.append(i)
        #             flag = 1
        #             break
        #     if flag == 0:
        #         has.append([i])

        # return has

        #SOL 2
        biglist = {}
        lst = []

        for i in strs:
            k = str(sorted(i))
            if k in biglist.keys():
                biglist[k].append(i)
            else:
                biglist[k] = [i]
        for i,j in biglist.items():
            lst.append(j)
        return lst


        # has, lst = {}, []

        # for i in strs:
        #     j = str(sorted(i))
        #     if j in has.keys():
        #         has[j].append(i)
        #     else:
        #         has[j] = [i]

        # for i in has.keys():
        #     lst.append(has[i])
        # return lst
        

        

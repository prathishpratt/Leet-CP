def findSimilarity(arr1, arr2, n, m):
    k = set(arr1 + arr2)
    
    return len(k - ((set(arr1)-set(arr2)) | (set(arr2)-set(arr1)))) , len(k)

    #Above is like venn diagram answer, remove the unwanted from the whole set


    # inter = 0
    # union = 0
    # dicti = {}

    # for i in range(0,len(arr1)):
    #     dicti[arr1[i]] = i
    #     union+=1
    
    # for i in range(0,len(arr2)):
    #     if arr2[i] in dicti.keys():
    #         inter +=1
    #     else:
    #         union+=1

    # return inter,union

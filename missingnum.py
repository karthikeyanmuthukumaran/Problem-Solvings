def missnum(arr):
    n=len(arr)+1

    totalsum=sum(arr)
    formula=n*(n+1)//2
    find=formula-totalsum
    return find


arr=[1,3,4,6,5]
print(missnum(arr))
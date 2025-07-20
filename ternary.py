def ternary_search(arr,tar):
    low=0
    high=len(arr)-1
    while low<=high:
        
        mid1=low+(high-low)//3
        mid2=high-(high-low)//3

        if arr[mid1]==tar:
            return mid1
        if arr[mid2]==tar:
            return mid2
        
        if tar<arr[mid1]:
            high=mid1-1
        elif tar>arr[mid2]:
            low=mid2+1
        else:
            low=mid1+1
            high=mid2-1

    return -1
def main():
    arr=[0,2,4,6,8,9,11,13]
    print(arr)

    try:
        tar=int(input("enter number to search:"))
    except ValueError:
        print("error enter as int")
    index=ternary_search(arr,tar)

    if index!=-1:
        print(f"{tar} is found at {index}")
    else:
        print("not found")

if __name__=="__main__":
    main()
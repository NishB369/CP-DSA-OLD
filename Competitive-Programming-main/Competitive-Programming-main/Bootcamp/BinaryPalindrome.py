def find_insertion_position(arr, n):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=(low+high)//2
        mid_val=arr[mid]
        
        if mid_val==n:
            return mid 
        elif mid_val<n:
            low=mid+1
        else:
            high=mid-1
    return low

binary_palindrome_list=[]

for num in range(1, 2**16 + 1):
    binary_num = bin(num)[2:] 
    s1=binary_num+binary_num[::-1]
    s2=s=binary_num+'0'+binary_num[::-1]
    s3=s=binary_num+'1'+binary_num[::-1]
    binary_palindrome_list.append(int(s1,2))
    binary_palindrome_list.append(int(s2,2))
    binary_palindrome_list.append(int(s3,2))
    

l=[1]+binary_palindrome_list
l.sort()

t=int(input())
for _ in range(t):
    n=int(input())
    m=find_insertion_position(l,n)
    a=n-l[m-1]
    b=l[m]-n
    if a<0:
        print(b)
    elif b<0:
        print(a)
    else:
        print(min(a,b))
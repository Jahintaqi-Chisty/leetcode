a=[1,2,8,9,10]
len =len(a) 
target =9
l = 0
u = len-1
position = l
while(l<=u):
    mid = l+((u-l)//2)
    if a[mid] == target:
        position = mid
        break
    else:
        if a[mid]< target:
            l = mid+1
        else:
            u = mid-1

print(f"Position is {position}")




# min = 0
# max = len-min
# for i in range(0,len-1):
#     if max==min:
#        print( max)
#     diff = (max - min)//2
#     mid =min +diff
#     if a[mid]== target:
#         print()
#     elif a[mid] > target:
#         min=0
#         max = mid
#     else :
#         min =mid+1
#         max = len
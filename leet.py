# def query_nums(nums):

#     for i in range(0,len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] == nums[j]:
#                 return(True)
            
#     return(False) 


# nums= [3,3]

# result = query_nums(nums)

# print(result)
# def towerOfHanoi(N , source, destination, auxiliary):
# 	if N==1:
# 		print("Move disk 1 from source",source,"to destination",destination)
# 		return
# 	towerOfHanoi(N-1, source, auxiliary, destination)
# 	print("Move disk",N,"from source",source,"to destination",destination)
# 	towerOfHanoi(N-1, auxiliary, destination, source)
		
# # Driver code
# N = 3
# towerOfHanoi(N,'A','B','C')

# def divideAndConquer_Max(arr, ind, len):
# 	maximum = -1;

# 	if (ind >= len - 2):
# 		if (arr[ind] > arr[ind + 1]):
# 			return arr[ind];
# 		else:
# 			return arr[ind + 1];


# 	maximum = divideAndConquer_Max(arr, ind + 1, len);

# 	if (arr[ind] > maximum):
# 		return arr[ind];
# 	else:
# 		return maximum;


# def divideAndConquer_Min(arr, ind, len):
# 	minimum = 0;
# 	if (ind >= len - 2):
# 		if (arr[ind] < arr[ind + 1]):
# 			return arr[ind];
# 		else:
# 			return arr[ind + 1];

# 	minimum = divideAndConquer_Min(arr, ind + 1, len);

# 	if (arr[ind] < minimum):
# 		return arr[ind];
# 	else:
# 		return minimum;


# if __name__ == '__main__':

# 	minimum, maximum = 0, -1;

# 	# array initialization
# 	arr = [6, 4, 8];

# 	maximum = divideAndConquer_Max(arr, 0, 3);
# 	minimum = divideAndConquer_Min(arr, 0, 3);

# 	print("The minimum number in the array is: ", minimum);
# 	print("The maximum number in the array is: ", maximum);


# def maxSubArray(nums):
# 	max_arr = nums[0] 
# 	curr = nums[0] 
# 	for i in range(1,len(nums)):
# 		curr = nums[i] if curr <0 else curr + nums[i]
# 		max_arr = max(max_arr,curr)
	
# 	# print(max_arr)
# 	return max_arr

# result = maxSubArray([5,4,-1,7,8])
# print(result)
num = [1,2,3]
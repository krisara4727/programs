#maximum continuous sub array with negative numbers in it
def maximum_continuous_sub_array(A):
	current_sum=0
	maximum_sum=0
	for i in A:
		current_sum=max(current_sum+i,i)
		maximum_sum=max(maximum_sum,current_sum)
	return maximum_sum
A=list(map(int,input().split()))
sum=maximum_continuous_sub_array(A)
print(sum)

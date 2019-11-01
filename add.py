#program to return two numbers that add upto k number using hash map
#with time complexity of O(n)

a=list(map(int,input().split()))
s=set()
sumi=int(input('enter the k number '))
for i in range(0,len(a)):
    temp=sumi-a[i]
    if(temp in s):
        print('pair with given sum '+str(sumi) + 'is ('+str(a[i])+","+str(temp)+")")
    s.add(a[i])
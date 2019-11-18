for i in range(k):
    if first_max<li[i]:
        first_max=li[i]
    elif first_max>li[i] and second_max<li[i]:
        second_max=li[i]
print(first_max)
for i in range(k,len(li)):
    if first_max==li[i-k]:
        if second_max>li[i]:
            print(second_max)
            first_max=second_max
        else:
            print(li[i])
            second_max,first_max=li[i],li[i]
    else:
        if first_max<li[i]:
            print(li[i])
            first_max,second_max=li[i],li[i]
        else:
            print(first_max)
            second_max=first_max
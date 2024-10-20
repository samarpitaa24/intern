x = [(10,9,8, 7), (6,5,4)]

for i in x :
    print(i)
    y = list(i)
    print(y)
    for j in range(len(y)) :
        print(j)
        print(y[j])
        y[j] -=1
        print(y[j])
        new_list = []
        t1 = tuple(y)
        new_list.append(t1)
    print(new_list )
#     abc = tuple(y)
# print (abc)
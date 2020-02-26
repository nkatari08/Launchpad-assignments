list=[1, 1, 2, 3, 4, 64, 35, 93, 35, 87, 4, 3]
final_list=[]
for i in list:
    if i not in final_list:
        final_list.append(i)

print(final_list)
search_num=int(input('enter the search element'))
list=[1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
for i in list:
    if (i==search_num) :
        print(list.index(i,0,11))
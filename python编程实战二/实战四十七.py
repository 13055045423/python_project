def angles(n):
    l=[[1]]
    #列表l有n个子列表，切记不可通过l=[[1]]*n实现
    for i in range(n):
        l.append([1])
    #从l[1]开始    
    for i in range(1,n):
        for x in range(1,i):
            l[i].append(l[i-1][x-1]+l[i-1][x])
        l[i].append(1)
    for i in range(n):
        print(l[i])
angles(9)

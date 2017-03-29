cases = int(input()) #number of cases
#print(cases)

for i in range(1, cases+1):
    #print("Case #{}".format(i))
    num_engines= int(input())
    #print(num_engines)
    engines=list()
    for j in range(1, num_engines+1):
        engines.append(str(input()))
    #print(engines)

    num_queries = int(input())
    #print(num_queries)

    queries=list()
    for k in range(1, num_queries+1):
        queries.append(str(input()))
    
    #print(queries)
    if(num_queries>0):
        uniquelist = list()
        uniquelist.append(queries[0])

        switches=0
        for l in range(1, num_queries):
            if queries[l] not in uniquelist:
                uniquelist.append(queries[l])
            if len(uniquelist) == num_engines:
                switches +=1
                uniquelist=[]
                uniquelist.append(queries[l])
    else:
        switches=0
    print("Case #{}: {}".format(i,switches))


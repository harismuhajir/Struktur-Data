def unOrderedSearch(listData,key):
    found = False
    i = 0
    index = []
    while i < len(listData) or not(found):
        if listData[i] == key:
            index.append(i)
            found = True
        i += 1
        if i == len(listData):
            break
    if found:
        return index
    else:
        return False

def OrderedSearch(listData,key):
    found = False
    i = 0
    stop = False
    count = 0
    while not(stop) and not(found):
        if i == len(listData) or listData[i] > key:
            stop = True
        elif listData[i] == key:
            index = []
            for j in range(i,len(listData)):
                if listData[j] == key:
                    index.append(j)
                else:
                    break
                count += 1
            found = True
        i += 1
        count += 1
    print("Counter=", count)
    if found:
        return index
    else:
        return False

a = [54,25,73,12,15,2,30,73]
b = [2,12,15,15,25,30,54,73]
print(unOrderedSearch(a,73))
print(OrderedSearch(b,15))

# Haris Muhajir Al Fatih | 190411100094 | 2B
def insertionSort(order,mode,listData):
    print("Data awal=", listData)
    if (mode == "awal"):
        for outIter in range(1, len(listData)):
            key = listData[outIter]
            print("[Iterasi ke-{}][Key: {}]".format(outIter, key))
            inIter = outIter - 1
            num = 1
            if (order == "asc"):
                while inIter != -1 and key <= listData[inIter]:
                    listData[inIter + 1] = listData[inIter]
                    print(num, "=", listData)
                    inIter -= 1
                    num += 1
            elif (order == "desc"):
                while inIter != -1 and key >= listData[inIter]:
                    listData[inIter + 1] = listData[inIter]
                    print(num, "=", listData)
                    inIter -= 1
                    num += 1
            listData[inIter + 1] = key
            print("Hasil=", listData)
    elif (mode == "akhir"):
        x = 1
        for outIter in range(len(listData) - 1, 0, -1):
            key = listData[outIter - 1]
            print("[Iterasi ke-{}][Key: {}]".format(x, key))
            x += 1
            inIter = outIter
            num = 1
            if (order == "asc"):
                while inIter != len(listData) and key >= listData[inIter]:
                    listData[inIter - 1] = listData[inIter]
                    print(num, "=", listData)
                    inIter += 1
                    num += 1
            elif (order == "desc"):
                while inIter != len(listData) and key <= listData[inIter]:
                    listData[inIter - 1] = listData[inIter]
                    print(num, "=", listData)
                    inIter += 1
                    num += 1
            listData[inIter - 1] = key
            print("Hasil=", listData)
    print("Data urut=", listData)

a = [10,5,7,4,9]
b = [10,5,7,4,9]
c = [10,5,7,4,9]
d = [10,5,7,4,9]
print("[---Ascending Awal---]")
insertionSort("asc","awal",a)
print()
print("[---Ascending Akhir---]")
insertionSort("asc","akhir",b)
print()
print("[---Descending Awal---]")
insertionSort("desc","awal",c)
print()
print("[---Descending Akhir---]")
insertionSort("desc","akhir",d)

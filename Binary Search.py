# Haris Muhajir Al Fatih | 190411100094 | 2B
def recBinarySearch(listData,first,last,key):
    if last >= first:
        mid = (last+first)//2
        if listData[mid] == key:
            result = []
            for i in range(first,last+1):
                if listData[i] == key:
                    result.append(i)
                else:
                    break
            return result
        elif listData[mid] > key:
            return recBinarySearch(listData,first,mid-1,key)
        elif listData[mid] < key:
            return recBinarySearch(listData,mid+1,last,key)
    else:
        return False

a = [2,12,15,25,30,43,54,54,60,73,73,73,73,73,90,90,90,100]
print(recBinarySearch(a,0,len(a)-1,73))

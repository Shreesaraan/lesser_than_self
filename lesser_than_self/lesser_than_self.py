def lesser_than_self(array):
    result=[]
    for i in range(len(array)):
        count=0
        for j in range(i+1,len(array)):
            if array[i]>array[j]:
                count+=1
        result.append(count)
    return result

array=list(map(int,input("Enter the Array Elements : ").split()))
print(lesser_than_self(array))
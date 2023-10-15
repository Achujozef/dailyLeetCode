array1= [1,3,5]
array2= [2,4,6]

def sorter(array1,array2):
    sorted=[]
    i=j = 0
    while i< len(array1) and j< len(array2):
        if array2[j]>array1[i]:
            sorted.append(array1[i])
            i+=1
        else:
            sorted.append(array2[j])
            j+=1
    while i <len(array1):
        sorted.append(array1[i])
        i+=1
    while j < len(array2):
        sorted.append(array2[j])
        j+=1
    return sorted

x=sorter(array1,array2)
print(x)
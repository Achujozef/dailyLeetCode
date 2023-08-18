#Write a function to find the second largest element in a list.

list1=[1,2,3,4,5,6,7,8]

def secondLargest(List):

    largest=max(List)
    print(largest)
    x=0
    for i in List:
   
        if i > x and i < largest:
            x=i
    return x

x=secondLargest(list1)
print(x)

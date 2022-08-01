#serach algorithms- linear

def linear(list1, n, key):  
  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
list1 = [1 ,3, 5, 4, 7, 9]  
key = 7  
n = len(list1)  
res = linear(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print(res)  



def linear(list1, n, key):  
  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
list1 = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
n = len(list1)  
res = linear(list1, n, key) 
if(res == -1):  
    print("Element not found")  
else:  
    print(res)  

print(linear(list1, 6))



def search(list1, x):
    for i in range(len(list1)):
        if list1[i] == x:
            return i
    return -1
list1 = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(search(list1, 6))


#binary search- recursion

def binary_search(searchList, searchTerm):
    searchList.sort()
    if len(searchList) == 0:
        return False

    middle = len(searchList) // 2
    if searchList[middle] == searchTerm:
        return True
    elif searchTerm < searchList[middle]:
        return binary_search(searchList[:middle], searchTerm)

    else:
        return binary_search(searchList[middle + 1:], searchTerm)

intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))

strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print("Lucy is in strlist:", binary_search(strlist, "Lucy"))

from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))



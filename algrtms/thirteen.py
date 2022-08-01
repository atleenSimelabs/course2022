#binary search-loop

def binary_search(searchList, searchTerm):
    searchList.sort()
    min = 0 #0
    max = len(searchList) - 1 #9
    while min <= max: #0<=9
        currentMiddle = (min + max) // 2 #9//2=4.5=5
        if searchList[currentMiddle] == searchTerm:#list[5]==19
            return True
        elif searchTerm < searchList[currentMiddle]: #23<19
            max = currentMiddle - 1
        else:
            min = currentMiddle + 1 #min=6
    return False

intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
#intlist=[1,3,12,17,19,23,51,57,62,64]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))

strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print("Lucy is in strlist:", binary_search(strlist, "Lucy"))

from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))



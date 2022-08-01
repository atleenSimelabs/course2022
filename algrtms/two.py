def count_down(start):
    if start <= 0:
        print(start)
    else:
        print(start)
        count_down(start - 1)
        
count_down(4)


def count_down2(start):
    for i in range(start+1):
        print(start)
        start-=1

count_down2(5)


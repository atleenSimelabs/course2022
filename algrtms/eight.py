#directory exploration

#  Listfiles(dir):
#     for file in dir:
#         print(file)
#     for folder in dir:
#         Listfiles(folder)


def count_down(start):
    if start <= 0:
        print(start)
    else:
        count_down(start - 1)
        print(start)

count_down(5)



def main():
    my_list = [1, 2, 3, 4, 5, 6]

    new_list = list(hmyMap(lambda x: (x + 1), my_list.copy()))

    print(my_list)
    print(new_list)


def hmyMap(f, list):
    for el in list:
        yield f(el)


# OTHER WAY TO DO IT
# def hmyMap2(f, list):
#     if len(list) == 0:
#         None
#     else:
#         first = list.pop()
#         yield f(first)
#         yield from hmyMap2(f, list)




main()

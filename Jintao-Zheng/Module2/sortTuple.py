def first(n):
    return n[0]


def sort_List_first(tuples):
    return sorted(tuples, key=first)


print(sort_List_first([(5, 2), (2, 1), (4, 4), (3, 2), (1, 2)]))
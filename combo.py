# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(list_one, list_two):
    tupled = ()
    indexed = 0
    listy = []
    for item in list_one:
        tupled = (list_one[indexed], list_two[indexed])
        listy.append(tupled)
        indexed = indexed + 1
    return listy

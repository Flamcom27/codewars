def comp(array1, array2):
    if array2 == None or array1 == None:
        return False   
    array1 = list(map(lambda a: a**2, array1))
    array1.sort()
    array2.sort()
    return array2 == array1
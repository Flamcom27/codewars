def persistence(n:int, a=[]) -> int:
    def mult(args, p=1):
        for i in args:
            p *= i
        return p
    while len(str(n)) != 1:
        n = mult([int(i) for i in str(n)])
        a.append(n)
    return len(a)
print(persistence(25))

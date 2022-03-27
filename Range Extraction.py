from ast import Pass, arg


def solution(args: list) -> str:
    def sort_args(args:list):
        args.append('')
        first_num = args[0]
        for i in range(1, len(args)):
            if first_num + args.index(args[i]) - args.index(first_num) == args[i]:
                continue
            else:
                if first_num+1 == args[i-1]:
                    yield f"{first_num}"
                    yield f"{args[i-1]}"
                else:
                    yield f"{first_num}-{args[i-1]}" if first_num != args[i-1] else f"{first_num}"
                first_num = args[i]
    return ','.join(sort_args(args))
print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
# -6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20

from for_cons_strings import strarr, should_equal, shouldnt_equal

def longest_consec(strarr:list, k:int) -> str:
    if k > len(strarr) or k <= 0:
        return ''
    strings = [strarr[i:k+i] + (strarr[0:k-len(strarr[i:k+i])]) if len(strarr[i::1]) < k  else strarr[i:k+i] for i in range(len(strarr))]
    print(list(map(lambda a: len(a), strings)))
    print(strings)
    strings = list(map(lambda a: ''.join(a), strings))
    max_string = max(strings, key=len)
    print(strings)
    # print(len(strarr)==len(strings))
    # print(strarr[-1])
    # print(True) if should_equal in strings else print(False)
    # print(True) if max_string in strings else print(False)
    # print(strings.index(should_equal), strings.index(max_string), len(strings))
    # print(len(should_equal))
    # print(len(max_string))
    # print(should_equal == max_string)
    # print(max_string==shouldnt_equal)
    # find_should_equal = ''.join(list(filter(lambda a: a==should_equal, strings)))
    # print(find_should_equal)
    # print(True) if find_should_equal == should_equal else print(False)
    # print(max_string == shouldnt_equal)
    # print(len(should_equal), len(max_string))
    # print(max_string)
    return max_string
print(longest_consec(["zone", "abig", "thet", "form", "libe", "zase", 'fggf'], 6))
# print(should_equal)
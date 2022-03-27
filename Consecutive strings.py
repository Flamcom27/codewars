def longest_consec(strarr:list, k:int) -> str:
    if k > len(strarr) or k <= 0:
        return ''
    strings = [strarr[i:k+i] + (strarr[0:k-len(strarr[i:k+i])]) if len(strarr[i::1]) < k  else strarr[i:k+i] for i in range(len(strarr))]
    strings = list(map(lambda a: ''.join(a), strings))
    max_string = max(strings, key=len)
    return max_string

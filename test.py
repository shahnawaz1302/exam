def longest_substring(s):
    char_set = set()
    max_len = 0
    curr_len = 0
    start = 0

    for i in range(len(s)):
        if s[i] not in char_set:
            char_set.add(s[i])
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
                start = i - curr_len + 1
        else:
            char_set.remove(s[i-curr_len])
            curr_len -= 1
    return s[start:start+max_len]

# test the function
print(longest_substring("abcaefgh"))


def min_window(s, t):
    if len(t) > len(s):
        return "NONE"

    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1

    left = 0
    count = 0
    min_len = float('inf')
    start = 0
    window = {}

    for right in range(len(s)):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1

        if ch in need and window[ch] <= need[ch]:
            count += 1

        while count == len(t):
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left

            old = s[left]
            window[old] -= 1

            if old in need and window[old] < need[old]:
                count -= 1

            left += 1

    if min_len == float('inf'):
        return "NONE"

    return s[start:start + min_len]


s = input()
t = input()

print(min_window(s, t))

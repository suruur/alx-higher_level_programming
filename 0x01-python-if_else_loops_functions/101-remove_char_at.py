def remove_char_at(s, n):
    if 0 <= n and n < len(s):
        return s[:n] + s[n + 1:]
    else:
        return s

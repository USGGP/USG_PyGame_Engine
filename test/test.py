def event1(n):
    ans = [i for i in range(int(n))]
    return ans

def event2(a, b):
    if len(b) < 40:
        b.append(a)
    return b
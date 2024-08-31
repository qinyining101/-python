def a(b):
    c = []

    def d(e, f, g):
        if not f:
            if h(e):
                c.append(e)
            return

        if not g and f.startswith("at"):
            d(e + "@", f[2:], True)
        if f.startswith("nospam") and len(f) >= 6:
            d(e, f[6:], g)
        d(e + f[0], f[1:], g)

    d("", b, False)
    return c
def h(i):
    if not i:
        return False

    if i.startswith(".") or i.endswith("."):
        return False

    if "@" not in i:
        return False
    j = i.find("@")
    if j <= 0 or j >= len(i) - 1:
        return False
    if not i[j - 1].isalpha() or not i[j + 1].isalpha():
        return False

    for k in i:
        if not k.islower() and k not in ".@":
            return False

    return True
def strcmp(a, b):
    if len(a) < len(b):
        return 1
    for i in range(len(a)):
        if a[i] < b[i]:
            return 1
    return 0
def quick_sort(strings):
    if len(strings) <= 1:
        return strings
    pivot = strings[0]
    equal = [s for s in strings if strcmp(s, pivot) == 0]
    less = [s for s in strings if strcmp(s, pivot) == -1]
    greater = [s for s in strings if strcmp(s, pivot) == 1]
    
    return quick_sort(less) + equal + quick_sort(greater)
l = input().strip()
m = quick_sort(a(l))
for n in m:
    print(n)
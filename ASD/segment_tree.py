from operator import itemgetter
n = int(input())
a = list(map(int, input().split()))
t = [0]*(4 * n)
def build(a, v, tl, tr):
    if tl == tr:
        t[v] = a[tl]
    else:
        tm = int((tl + tr) / 2)
        build(a, 2 * v + 1, tl, tm)
        build(a, 2 * v + 2, tm + 1, tr)
        t[v] = t[2 * v + 1] + t[2 * v + 2]
def sum(v, tl, tr, l, r):
    if tl > r or tr < l:
        return 0
    if l <= tl and tr <= r:
        return t[v]
    else:
        tm = int((tl + tr) / 2)
        return sum(2 * v + 1, tl, tm, l, r) + sum(2 * v + 2, tm + 1, tr, l, r)
def update(v, tl, tr, pos, val):
    if tl == tr:
        t[v] = val
    else:
       
        tm = int((tl + tr) / 2)
        if pos <= tm:
            update(2 * v + 1, tl, tm, pos, val)
        else:
            update(2 * v + 2, tm + 1, tr, pos, val)
        t[v] = t[2 * v + 1] + t[2 * v + 2]
 

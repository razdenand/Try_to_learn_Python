a = []
ans = 0
n, m = map(int, input().split())
used = []
for i in range(n):
    kek = list(map(int, input().split()))
    buf = []
    for j in range(len(kek)):
        if kek[j] == 1:
            buf.append(j)
    a.append(buf)
for i in range(n):
    used.append(0)
    
def dfs(s):
    used[s] = 1
    global ans
    ans += 1
    for i in range(len(a[s])):
        if(used[a[s][i]] == 0):
            dfs(a[s][i])
dfs(m - 1)
print (ans)

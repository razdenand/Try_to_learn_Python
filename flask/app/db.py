from Classes import *

ans = db.q_fetchall('select count(id) from quest;')
print(ans[0]['count(id)'])
print(type(ans))
if ans == ():
    print('kek')
from collections import defaultdict
import reverse_geocoder as rg
uid = ''
buffer_query = ''
first_char = ''
local = ''
gps = ''
line_buf = '' 
russian_query = defaultdict(int)
english_query = defaultdict(int)
query_in_russia = []
def is_ru(buf):
    if buf.find('ru') != -1:
        return True
    else:
        return False
def find_country(coordinates):
    ans = rg.search(coordinates, mode=1)
    return ans[0]['cc']

def is_query(log, first_char, uid):
    if log[-1] != uid and uid != '':
        return True
    if log[0][1] != first_char and first_char != '':
        return True
    return False
with open("test.txt") as f:
    for line in f:
        log = list(line.split(';'))
        b = gps.replace('[', '').replace(']', '')
        coordinates = list(reversed((b.split(','))))
        if is_query(log, first_char, uid) and len(buffer_query) > 4:
            if is_ru(local):
                russian_query[buffer_query] += 1
            if not is_ru(local):
                english_query[buffer_query] += 1
            if gps != "None" and gps != '':
                if find_country(coordinates) == "RU":
                    query_in_russia.append(buffer_query)
        buffer_query = log[0]
        local = log[2]
        gps = log[3]
        uid = log[-1]
        first_char = log[0][1]
        log.clear()
        line_buf = line
print(sorted(dict(russian_query).items(), key = lambda x : x[1], reverse = True))
print(sorted(dict(english_query).items(), key = lambda x : x[1], reverse = True))
print(query_in_russia)

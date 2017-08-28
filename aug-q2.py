# Python 2.7
# Aug code jam, question 2
# Created on 8/26/2017, Lin Bin


def cal_count(s, pos, p, pos_len, a, c):
    # s is the list of the characters in an ID
    import calendar
    i = p + 1
    count = c
    for s[pos[p]] in lst[pos[p]]:
        if i < pos_len:
            count = cal_count(s, pos, i, pos_len, a, count)
        else:
            YYYY = int(''.join([s[4],s[5],s[6],s[7]]))
            MM = int(''.join([s[2],s[3]]))
            DD = int(''.join([s[0],s[1]]))
            if YYYY == 0:
                continue
            if MM == 0 or MM >12:
                continue
            if DD == 0 or DD >31:
                continue
            if MM in [4,6,9,11] and DD > 30:
                continue
            if MM == 2:
                if DD > 29:
                    continue
                if DD > 28 and not calendar.isleap(YYYY):
                    continue
            a1 = cal_a(s)
            if a1 == a:
                count += 1

    return count

def cal_a(ss):
    num_s = []
    for x in ss:
        num_s.append(int(x))
    h = (10*num_s[0]+9*num_s[1]+8*num_s[2]+7*num_s[3]+6*num_s[4]+5*num_s[5]+4*num_s[6]+3*num_s[7]+2*num_s[8]+10*num_s[9]+9*num_s[10]+8*num_s[11]+7*num_s[12]+6*num_s[13]+5*num_s[14]+4*num_s[15]+3*num_s[16]+2*num_s[17])%19
    if h <= 9:
        a = h
    else:
        a = 19 - h
    return a

import time

id_1 = '1B11111111111111116'
start = time.clock()

lst = range(19)
for i in range(19):
    if i == 0:
        lst[i] = range(4)
        for li, lv in enumerate(lst[i]):
            lst[i][li] = str(lv)
        continue
    if i == 1:
        lst[i] = range(10)
        for li, lv in enumerate(lst[i]):
            lst[i][li] = str(lv)
        continue
    if i == 2:
        lst[i] = range(2)
        for li, lv in enumerate(lst[i]):
            lst[i][li] = str(lv)
        continue
    lst[i] = range(10)
    for li, lv in enumerate(lst[i]):
        lst[i][li] = str(lv)



check_d = id_1[-1]

if check_d != 'B':
    num_b = id_1.count('B')
    pos_b = []

    if num_b >= 1:
        pos_b.append(id_1.find('B'))
        for i in range(1, num_b):
            pos_b.append(id_1.find('B',pos_b[i-1]+1))
    print pos_b # to be deleted

    s = []
    for j in iter(id_1):
        s.append(j)
    cc = cal_count(s, pos_b, 0, len(pos_b), check_d, 0)
    print 'cc:',cc, time.clock()-start # to be deleted
else:
    part_1 = id_1[:8]
    part_2 = id_1[8:18]
    num_b_p2 = part_2.count('B')
    count_p2 = 10**num_b_p2

    pos_b_p1 = []
    num_b_p1 = part_1.count('B')
    if num_b_p1 >=1:
        pos_b_p1.append(part_1.find('B'))
        for y in range(1, num_b_p1):
            pos_b_p1.append(part_1.find('B',pos_b_p1[y-1]+1))

        s_p1 = []
        for z in iter(part_1):
            s_p1.append(z)
        count_p1 = part_count() # a new function need be defined
    else:
        count_p1 = 1
# Python 2.7
# Aug code jam, question 2
# Created on 8/26/2017, Lin Bin

def cal_count(s, pos, p, pos_len, a, count):
    import calendar
    i = p + 1
    for s[pos] in lst[pos]:
        if i < pos_len:
            cal_count(s, pos_b[i], i, pos_len, a)
        else:
            YYYY = int(''.join(s[4],s[5],s[6],s[7]))
            MM = int(''.join(s[2],s[3]))
            DD = int(''.join(s[0],s[1]))
            if YYYY == 0:
                continue
            if MM == 0 or MM >12:
                continue
            if DD == 0 or DD >31:
                continue
            if MM in [4,6,9,11] and DD > 30:
                continue
            if not calendar.isleap(YYYY):
                if MM == 2 and DD > 28:
                    continue
            else:
                if MM == 2 and DD > 29:
                    continue
            a1 = cal_A(s)
            if a1 == a:
                count += 1
    return count

def cal_A(ss):
    s = []
    for x in ss:
        s.append(int(x))
    h = (10*s[0]+9*s[1]+8*s[2]+7*s[3]+6*s[4]+5*s[5]+4*s[6]+3*s[7]+2*s[8]+10*s[9]+9*s[10]+8*s[11]+7*s[12]+6*s[13]+5*s[14]+4*s[15]+3*s[16]+2*s[17])%19
    if h <= 9:
        a = h
    else:
        a = 19 - h
    return a

id_1 = '0101100100000000006'
if id_1 != 'B':
    a = int(id_1[-1])

lst = range(19)
for i in range(19):
    if i == 0:
        lst[i] = range(4)
        continue
    if i == 1:
        lst[i] = range(10)
        continue
    if i == 2:
        lst[i] = range(2)
        continue
    lst[i] = range(10)

s = []
for j in range(len(id_1)):
    s.append(id_1[j])

print

part_1 = id_1[:8]
part_2 = id_1[8:18]
check_d = id_1[-1]

num_b = id_1.count('B')
pos_b = []
pos_b1 = None

if num_b >= 1:
    pos_b1 = id_1.find('B')
if num_b > 1:
    for i in range(num_b):
        pos_b.append(id_1.find('B',pos_b1+i))

print s
print pos_b1
print pos_b

print cal_A(s)

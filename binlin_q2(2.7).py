# Python 2.7
# Aug code jam, question 2
# Created on 8/26/2017, Lin Bin

def calwithmod(mod_s, pos, pos_index, pos_len, a, mod_c):
    global modlst
    global lst
    mod_count = mod_c
    pos_idx = pos_index + 1
    for mod_s[pos[pos_index]] in lst[pos[pos_index]]:
        if pos_idx < pos_len:
            mod_count = calwithmod(mod_s, pos, pos_idx, pos_len, a, mod_count)
        else:
            YYYY = int(''.join([s[4], s[5], s[6], s[7]]))
            MM = int(''.join([s[2], s[3]]))
            DD = int(''.join([s[0], s[1]]))
            if YYYY == 0:
                if pos[pos_index] != 7:
                    break
                else:
                    continue
            if MM == 0:
                if pos[pos_index] not in [2,3]:
                    break
                else:
                    continue
            if MM > 12:
                break
            if DD > 31:
                break
            if DD == 0:
                if pos[pos_index] not in [0,1]:
                    break
                else:
                    continue
            if MM in [4, 6, 9, 11] and DD > 30:
                if pos[pos_index] > 3:
                    break
                else:
                    continue
            if MM == 2:
                if DD > 29:
                    if pos[pos_index] > 3:
                        break
                    else:
                        continue
                if DD > 28 and not calendar.isleap(YYYY):
                    if pos[pos_index] > 7:
                        break
                    else:
                        continue
            m1 = cal_mod(mod_s, pos[pos_index])
            if m1+a <= 19:
                mod1 = 19-m1-a
            else:
                mod1 = 38-m1-a
            if m1-a <= 0:
                mod2 = a-m1
            else:
                mod2 = 19+a-m1
            if mod1 in modlst[pos[pos_index]]:
                mod_count += 1
            if mod2 in modlst[pos[pos_index]]:
                mod_count += 1
            break
    return mod_count


def part1_count(s, pos, p, pos_len, c):
    import calendar
    global lst
    i = p + 1
    cnt = c
    for s[pos[p]] in lst[pos[p]]:
        if i < pos_len:
            cnt = part1_count(s, pos, i, pos_len, cnt)
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
            cnt += 1
    return cnt

def cal_mod(mods, pos):
    num_s = []
    for x in mods:
        num_s.append(int(x))
    num_s[pos] = 0
    h = (10*num_s[0]+9*num_s[1]+8*num_s[2]+7*num_s[3]+6*num_s[4]+5*num_s[5]+4*num_s[6]+3*num_s[7]+2*num_s[8]+10*num_s[9]+9*num_s[10]+8*num_s[11]+7*num_s[12]+6*num_s[13]+5*num_s[14]+4*num_s[15]+3*num_s[16]+2*num_s[17])%19
    return h

if __name__ == '__main__':

    id_1 = raw_input().strip()
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

    modlst = [[] for m in range(19)]
    for ll in range(9):
        for l in lst[ll]:
            modlst[ll].append(((10-ll)*int(l))%19)
    for ll in range(9,19):
        for l in lst[ll]:
            modlst[ll].append(((19-ll)*int(l))%19)

    check_d = id_1[-1]

    if check_d != 'B':
        check_num = int(check_d)
        num_b = id_1.count('B')
        pos_b = []

        if num_b >= 1:
            pos_b.append(id_1.find('B'))
            for i in range(1, num_b):
                pos_b.append(id_1.find('B',pos_b[i-1]+1))
        s = []
        for j in iter(id_1):
            s.append(j)
        cc = calwithmod(s, pos_b, 0, len(pos_b), check_num, 0)
        print cc
    else:
        part_1 = id_1[:8]
        part_2 = id_1[8:18]
        num_b_p2 = part_2.count('B')
        count_p2 = 10**num_b_p2

        pos_b_p1 = []
        num_b_p1 = part_1.count('B')
        if num_b_p1 == 8:
            count_p1 = 3652059
        else:
            if num_b_p1 >=1:
                pos_b_p1.append(part_1.find('B'))
                for y in range(1, num_b_p1):
                    pos_b_p1.append(part_1.find('B',pos_b_p1[y-1]+1))

                s_p1 = []
                for z in iter(part_1):
                    s_p1.append(z)
                count_p1 = part1_count(s_p1, pos_b_p1, 0, len(pos_b_p1), 0) # to calucate the posibilities in the 1st 8 digtals
            else:
                count_p1 = 1

        count_total = count_p2*count_p1
        print count_total

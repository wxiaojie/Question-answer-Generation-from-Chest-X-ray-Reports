def concatwords(wordslist):
    if wordslist == []:
        sentence = ''
    else:
        sentence = wordslist[0]
        for i in range(1,len(wordslist)):
            sentence += ' ' + wordslist[i]
    return sentence

def changeinvolve(temp_p, temp_s):
    if temp_p.count('involving') > 0:
        temp_i = [i for i, v in enumerate(temp_p) if v == 'involving']
        for i in temp_i:
            in_index = i
            inc_index = temp_p[in_index:].index('.') + in_index
            if temp_p[in_index:].count('y') > 0:
                iny_index = temp_p[in_index:].index('y') + in_index
            else:
                iny_index = len(temp_p)
            if inc_index < iny_index:
                end_index = inc_index
            else:
                end_index = iny_index
            if temp_p[in_index:end_index].count('l') > 0 and temp_p[in_index:end_index].count('d') == 0:
                temp_p[in_index] = 'in'
                temp_s[in_index] = 'in'
            elif temp_p[in_index:end_index].count('d') > 0:
                temp_p[in_index] = '.'
                temp_s[in_index] = '.'
            else:
                temp_p[in_index] = ''
                temp_s[in_index] = ''
    return temp_p, temp_s


def changesuperimpose(temp_p, temp_s):
    if temp_p.count('superimposed') > 0:
        in_index = temp_p.index('superimposed')
        inc_index = temp_p[in_index:].index('.') + in_index
        y_count = temp_p[in_index-5:in_index].count('y')
        if y_count == 0 and temp_p[in_index:inc_index].count('d') > 0:
            temp_p[in_index] = '.'
            temp_s[in_index] = '.'
        elif y_count == 0 and temp_p[in_index:inc_index].count('o') > 0:
            temp_p[in_index] = '. s'
            temp_s[in_index] = '. superimposed'
    return temp_p, temp_s


prep = ['and', ',', '.', 'or', 'in', 'within']

def deletetail(patternlist):
    while patternlist != [] and prep.count(patternlist[-1]) > 0:
        patternlist = patternlist[:-1]
    return patternlist

def deletetails(slist):
    if slist != [] and slist[-4:] == [',', 'small', 'left', 'sided']:
        slist = slist[:-4]
    elif slist != [] and slist[-4:] == [',', ',','small', 'left']:
        slist = slist[:-4]
    return slist

def deletehead(patternlist):
    while patternlist != [] and prep.count(patternlist[0]) > 0:
        patternlist = patternlist[1:]
    return patternlist

def nood(patternlist):
    if patternlist.count('o') == 0 and patternlist.count('d') == 0:
        patternlist = []
    return patternlist

def nochange(slist, plist):
    if len(slist) >1 and slist[0] == 'no' and slist[1] == 'change':
        slist = slist[2:]
        plist = plist[2:]
    return slist, plist

def negativefree(slist, plist):
    if slist.count('free') > 0 and slist[slist.index('free'):].count('air') == 0:
        plist[slist.index('free')] = 'y'
        slist[slist.index('free')] = 'no'
    return slist, plist

def negativeclear(slist, plist):
    if slist.count('clear') > 0 and len(slist) > slist.index('clear')+1 and plist[slist.index('clear')+1] != ',' \
            and plist[slist.index('clear'):].count('d') > 0 and plist[slist.index('clear'):].count('y') == 0:
        plist[slist.index('clear')] = 'y'
        slist[slist.index('clear')] = 'no'
    elif slist.count('clearing') > 0:
        plist[slist.index('clearing')] = 'y'
        slist[slist.index('clearing')] = 'no'
    elif slist.count('cleared') > 0:
        plist[slist.index('cleared')] = 'y'
        slist[slist.index('cleared')] = 'no'
    return slist, plist

def deleteand(slist, plist):
    if plist.count('and') > 0 and plist[plist.index('and')+1] == 'in':
        plist.remove('and')
        slist.remove('and')
    elif plist == ['l','l','and','d']:
        plist.remove('and')
        slist.remove('and')
    elif plist == ['l','l','and','o']:
        plist.remove('and')
        slist.remove('and')
    elif plist == ['y','y','and']:
        plist.remove('and')
        slist.remove('and')
    return slist, plist

def deleteor(slist, plist):
    if plist.count('or') > 0 and plist[plist.index('or')-1] == 'y':
        plist.remove('or')
        slist.remove('or')
    return slist, plist

def deletecomma(slist, plist):
    if len(plist) > 0 and plist[0] == ',':
        plist.remove(',')
        slist.remove(',')
    elif plist.count(',') > 0 and plist[plist.index(',')+1] == 'in':
        plist.remove(',')
        slist.remove(',')
    elif plist.count(',') > 0 and plist[plist.index(',')+1] == ',' and plist[plist.index(',')+2] == 'in':
        plist.remove(',')
        slist.remove(',')
        plist.remove(',')
        slist.remove(',')
    elif len(plist) > 2 and plist[:2] == ['y', ',']:
        plist = plist[2:]
        slist = slist[2:]
    elif len(plist) > 3 and plist[:3] == ['y', 'y', ',']:
        plist = plist[3:]
        slist = slist[3:]
    elif len(plist) > 2 and plist[-2:] == [',', 'y']:
        plist = plist[:-2]
        slist = slist[:-2]
    elif len(plist) > 3 and plist[-3:] == [',', 'y', 'y']:
        plist = plist[:-3]
        slist = slist[:-3]
    elif plist.count(',') > 0 and plist[:plist.index(',')].count('o') == 0 and plist[plist.index(',')-1] == 's' and plist[plist.index(',')+1] == 's':
        plist.remove(',')
        slist.remove(',')
    elif plist.count(',') > 0 and plist[plist.index(','):].count('o') == 0 and plist[plist.index(',')-1] == 's' and plist[plist.index(',')+1] == 's':
        plist.remove(',')
        slist.remove(',')
    return slist, plist


def extray(p_line, s_line):
    if p_line.count('y') > 0 and len(p_line) > p_line.index('y') + 2 and p_line[p_line.index('y')+1] == 'y' and \
            p_line[p_line.index('y')+2] == 'y' and \
            p_line[p_line.index('y'):].count('o') == 0 and p_line[p_line.index('y'):].count('d') == 0:
        s_line = s_line[:p_line.index('y')]
        p_line = p_line[:p_line.index('y')]
    elif p_line.count('y') > 0 and len(p_line) > p_line.index('y') + 2 and p_line[p_line.index('y')+1] == 'y' and \
            p_line[p_line.index('y')+2] == 'y' and \
            p_line[p_line.index('y'):].count('o') > 0:
        y_index = p_line.index('y')
        p_line.remove('y')
        s_line.remove(s_line[y_index])
    elif p_line.count('y') > 0 and len(p_line) > p_line.index('y') + 2 and p_line[p_line.index('y')+1] == 'y' and \
            p_line[p_line.index('y')+2] == 'y' and \
            p_line[p_line.index('y'):].count('d') > 0:
        y_index = p_line.index('y')
        p_line.remove('y')
        s_line.remove(s_line[y_index])
    return p_line, s_line


def gettemp(line,s,e,share):
    temp = line[s:e]
    temp.extend(share)
    return temp

def splitsharewithin(p_line, s_line):
    if p_line.count('and') > 0 and p_line.count('within') > 0 and p_line.index('and') < p_line.index('within'):
        share_p = p_line[p_line.index('within'):]
        share_s = s_line[s_line.index('within'):]
        p = []
        s = []
        if p_line.count(',') > 0 and p_line.count('and') > 0 and p_line.index(',') < p_line.index('and'):
            p.append(gettemp(p_line,0,p_line.index(','),share_p))
            p.append(gettemp(p_line,p_line.index(',')+1,p_line.index('and'),share_p))
            p.append(gettemp(p_line,p_line.index('and')+1,p_line.index('within'), share_p))
            s.append(gettemp(s_line,0,s_line.index(','), share_s))
            s.append(gettemp(s_line,s_line.index(',') + 1,s_line.index('and'), share_s))
            s.append(gettemp(s_line,s_line.index('and') + 1,s_line.index('within'), share_s))
        else:
            p.append(gettemp(p_line,0,p_line.index('and'), share_p))
            p.append(gettemp(p_line,p_line.index('and') + 1,p_line.index('within'), share_p))
            s.append(gettemp(s_line,0,s_line.index('and'), share_s))
            s.append(gettemp(s_line,s_line.index('and') + 1,s_line.index('within'), share_s))
    elif p_line.count('and') > 0 and p_line.count('within') > 0 and p_line.count(',') > 0 and p_line.index('and') > p_line.index(',') > p_line.index('within'):
        p = []
        s = []
        p.append(p_line[:p_line.index(',')])
        p.append(p_line[p_line.index(',')+1:])
        s.append(s_line[:s_line.index(',')])
        s.append(s_line[s_line.index(',')+1:])
    else:
        p = [concatwords(p_line).split(' ')]
        s = [concatwords(s_line).split(' ')]
    return p, s

def splityc(p_line, word):
    temp = concatwords(p_line).split(',')
    word = ' ' + word + ' '
    temp_word = temp[len(temp) - 1].split(word)
    temp.remove(temp[len(temp) - 1])
    temp.extend(temp_word)
    return temp

def splitsharey(p_line, s_line, word):
    if p_line.count('y') > 1 and p_line[0] == 'y' and p_line[1] == 'y' and p_line.count(word) > 0 and p_line.index('y') < p_line.index(word):
        share_p = p_line[p_line.index('y'):p_line.index('y')+2]
        share_s = s_line[p_line.index('y'):p_line.index('y')+2]
        p = []
        s = []
        if p_line.count(',') > 0 and p_line.count(word) > 0 and p_line.index(',') < p_line.index(word):
            temp_p = splityc(p_line[p_line.index('y')+2:], word)
            temp_s = splityc(s_line[p_line.index('y') + 2:], word)
            for i in range(len(temp_p)):
                p.append((concatwords(share_p) + ' ' + temp_p[i].lstrip().rstrip()).split(' '))
                s.append((concatwords(share_s) + ' ' + temp_s[i].lstrip().rstrip()).split(' '))
        else:
            p.append((concatwords(share_p) + ' ' + concatwords(p_line[p_line.index('y')+2:p_line.index(word)])).split(' '))
            p.append((concatwords(share_p) + ' ' + concatwords(p_line[p_line.index(word) + 1:len(p_line)])).split(' '))
            s.append((concatwords(share_s) + ' ' + concatwords(s_line[p_line.index('y')+2:s_line.index(word)])).split(' '))
            s.append((concatwords(share_s) + ' ' + concatwords(s_line[s_line.index(word) + 1:len(s_line)])).split(' '))
    elif p_line.count('y') > 0 and p_line[0] == 'y' and p_line.count(word) > 0 and p_line.count('in') > 0 and \
            p_line.index('in') < p_line.index(word):
        p = [concatwords(p_line).split(' ')]
        s = [concatwords(s_line).split(' ')]
    elif p_line.count('y') > 0 and p_line[0] == 'y' and p_line.count(word) > 0 and p_line[1] != 'y':
    # elif p_line.count('y') > 0 and p_line[0] == 'y' and p_line.count(word) > 0 and p_line.index('y') < p_line.index(word):
        share_p = p_line[p_line.index('y')]
        share_s = s_line[p_line.index('y')]
        p = []
        s = []
        if p_line.count(',') > 0 and p_line.count(word) > 0 and p_line.index(',') < p_line.index(word):
            temp_p = splityc(p_line[p_line.index('y') + 1:], word)
            temp_s = splityc(s_line[p_line.index('y') + 1:], word)
            for i in range(len(temp_p)):
                p.append((share_p + ' ' + temp_p[i].lstrip().rstrip()).split(' '))
                s.append((share_s + ' ' + temp_s[i].lstrip().rstrip()).split(' '))
        else:
            p.append((share_p + ' ' + concatwords(p_line[p_line.index('y')+1:p_line.index(word)])).split(' '))
            p.append((share_p + ' ' + concatwords(p_line[p_line.index(word) + 1:])).split(' '))
            s.append((share_s + ' ' + concatwords(s_line[p_line.index('y')+1:s_line.index(word)])).split(' '))
            s.append((share_s + ' ' + concatwords(s_line[s_line.index(word) + 1:])).split(' '))
    elif p_line.count('y') > 0 and p_line[0] == 'y' and p_line.count(',') > 0 and p_line.index('y') < p_line.index(','):
        share_p = p_line[p_line.index('y')]
        share_s = s_line[p_line.index('y')]
        p = []
        s = []
        temp_p = concatwords(p_line[p_line.index('y') + 1:]).split(',')
        temp_s = concatwords(s_line[p_line.index('y') + 1:]).split(',')
        for i in range(len(temp_p)):
            p.append((share_p + ' ' + temp_p[i].lstrip().rstrip()).split(' '))
            s.append((share_s + ' ' + temp_s[i].lstrip().rstrip()).split(' '))
    else:
        p = [concatwords(p_line).split(' ')]
        s = [concatwords(s_line).split(' ')]
    return p, s


def splitys(p_line, s_line):
    if p_line.count('y') > 0 and p_line.index('y') > 0 and p_line[p_line.index('y')+1] == 's' and \
            p_line.count('and') > 0 and p_line.index('and') < p_line.index('y'):
        share_p = p_line[p_line.index('y'):]
        share_s = s_line[p_line.index('y'):]
        p = []
        s = []
        # if p_line.count(',') > 0 and p_line.count(word) > 0 and p_line.index(',') < p_line.index(word):
        #     temp_p = splityc(p_line[p_line.index('y')+2:], word)
        #     temp_s = splityc(s_line[p_line.index('y') + 2:], word)
        #     for i in range(len(temp_p)):
        #         p.append((concatwords(share_p) + ' ' + temp_p[i].lstrip().rstrip()).split(' '))
        #         s.append((concatwords(share_s) + ' ' + temp_s[i].lstrip().rstrip()).split(' '))
        p.append((concatwords(p_line[:p_line.index('and')]) + ' ' + concatwords(share_p)).split(' '))
        p.append((concatwords(p_line[p_line.index('and') + 1:p_line.index('y')]) + ' ' + concatwords(share_p)).split(' '))
        s.append((concatwords(s_line[:p_line.index('and')]) + ' ' + concatwords(share_s)).split(' '))
        s.append((concatwords(s_line[p_line.index('and') + 1:p_line.index('y')]) + ' ' + concatwords(share_s)).split(' '))
    else:
        p = [concatwords(p_line).split(' ')]
        s = [concatwords(s_line).split(' ')]
    return p, s


def splitmidy(p_line, s_line, mid):
    # if p_line[mid:].count('y') > 0 and p_line[p_line[mid:].index('y') + mid:].count('d') > 0 and p_line[:mid].count('l') != 0:
    if s_line[0] == 'no' and p_line.count('y') == 2 and p_line[p_line[mid:].index('y') + mid:].count('d') > 0 and \
            s_line[p_line[mid:].index('y') + mid] == 'suspicious':
        s_line = concatwords(s_line[1:])
        p_line = concatwords(p_line[1:])
        temp_cs = s_line.split(' , ')
        temp_s = []
        for i in temp_cs:
            if i.count(' or ') > 0:
                temp_s.extend(i.split(' or '))
            else:
                temp_s.append(i)
        temp_cp = p_line.split(' , ')
        temp_p = []
        for i in temp_cp:
            if i.count(' or ') > 0:
                temp_p.extend(i.split(' or '))
            else:
                temp_p.append(i)
        p = []
        s = []
        for i in range(len(temp_p)):
            t_p = ('y ' + temp_p[i]).split(' ')
            t_s = ('no ' + temp_s[i]).split(' ')
            p.append(t_p)
            s.append(t_s)
    elif p_line[0] == 'y' and p_line.count('y') > 2 and p_line[p_line[mid:].index('y') + mid:].count('d') > 0:
        temp = [0]
        temp_c = [i for i, v in enumerate(p_line) if v == 'y']
        temp.extend(temp_c)
        temp.append(len(p_line))
        p = []
        s = []
        for i in range(len(temp) - 1):
            p.append(p_line[temp[i]:temp[i + 1]])
            s.append(s_line[temp[i]:temp[i + 1]])
        p.remove([])
        s.remove([])
    elif p_line[mid:].count('y') > 0 and p_line[p_line[mid:].index('y') + mid:].count('d') > 0:
        index_y = p_line[mid:].index('y')+mid
        p = []
        s = []
        if p_line[:index_y].count('y') > 0:
            temp_p, temp_s = splitsharey(p_line[:index_y], s_line[:index_y], 'and')
            p.extend(temp_p)
            s.extend(temp_s)
        else:
            p.append(p_line[:index_y])
            s.append(s_line[:index_y])
        if p_line[index_y:].count('or') > 0:
            p_temp, s_temp = splitsharey(p_line[index_y:], s_line[index_y:], 'or')
        else:
            p_temp, s_temp = splitsharey(p_line[index_y:], s_line[index_y:], 'and')
        p.extend(p_temp)
        s.extend(s_temp)
    # elif p_line[mid:].count('y') > 0 and p_line[p_line[mid:].index('y') + mid:].count('o') > 0 and p_line[:mid].count('l') != 0:
    elif p_line[mid:].count('y') > 0 and p_line[p_line[mid:].index('y') + mid:].count('o') > 0:
        index_y = p_line[mid:].index('y')+mid
        p = []
        s = []
        if p_line[:index_y].count('y') > 0:
            temp_p, temp_s = splitsharey(p_line[:index_y], s_line[:index_y], 'and')
            p.extend(temp_p)
            s.extend(temp_s)
        else:
            p.append(p_line[:index_y])
            s.append(s_line[:index_y])
        if p_line[index_y:].count('or') > 0:
            p_temp, s_temp = splitsharey(p_line[index_y:], s_line[index_y:],'or')
        else:
            p_temp, s_temp = splitsharey(p_line[index_y:], s_line[index_y:], 'and')
        p.extend(p_temp)
        s.extend(s_temp)
    elif p_line[mid:].count('y') > 0 and p_line[p_line[mid:].index('y') + mid:].count('l') > 0:
        index_y = p_line[mid:].index('y') + mid
        p = []
        s = []
        p.append(p_line[:index_y])
        s.append(s_line[:index_y])
    else:
        p = [concatwords(p_line).split(' ')]
        s = [concatwords(s_line).split(' ')]
    return p, s


def partyc(p_line,s_line):
    if p_line.count(',') > 0 and p_line[p_line.index(','):].count('y') > 0 and p_line[p_line.index(','):].count('o') > 0 \
            and p_line[:p_line.index(',')].count('o') > 0:
        p = []
        s = []
        temp_p, temp_s = splitsharey(p_line[:p_line.index(',')], s_line[:p_line.index(',')], 'and')
        p.extend(temp_p)
        s.extend(temp_s)
        p.append(p_line[p_line.index(',')+1:])
        s.append(s_line[p_line.index(',')+1:])
    elif p_line.count(',') > 0 and p_line[p_line.index(','):].count('y') > 0 and p_line[p_line.index(','):].count('d') > 0 \
            and p_line[:p_line.index(',')].count('o') > 0:
        p = []
        s = []
        temp_p, temp_s = splitsharey(p_line[:p_line.index(',')], s_line[:p_line.index(',')], 'and')
        p.extend(temp_p)
        s.extend(temp_s)
        p.append(p_line[p_line.index(',')+1:])
        s.append(s_line[p_line.index(',')+1:])
    elif p_line.count(',') > 0 and p_line[p_line.index(','):].count('y')>0 and p_line[p_line.index(','):].count('o')>0 \
            and p_line[:p_line.index(',')].count('d')>0:
        p = []
        s = []
        temp_p, temp_s = splitsharey(p_line[:p_line.index(',')], s_line[:p_line.index(',')], 'and')
        p.extend(temp_p)
        s.extend(temp_s)
        p.append(p_line[p_line.index(',')+1:])
        s.append(s_line[p_line.index(',')+1:])
    elif p_line.count(',') > 0 and p_line[p_line.index(','):].count('y')>0 and p_line[p_line.index(','):].count('d')>0 \
            and p_line[:p_line.index(',')].count('d')>0:
        p = []
        s = []
        temp_p, temp_s = splitsharey(p_line[:p_line.index(',')], s_line[:p_line.index(',')], 'and')
        p.extend(temp_p)
        s.extend(temp_s)
        p.append(p_line[p_line.index(',')+1:])
        s.append(s_line[p_line.index(',')+1:])
    elif p_line.count(',') > 0 and p_line[p_line.index(','):].count('y')>0 and p_line.index(',')>1:
        p = []
        s = []
        temp_p, temp_s = splitsharey(p_line[:p_line.index(',')], s_line[:p_line.index(',')], 'and')
        p.extend(temp_p)
        s.extend(temp_s)
        p.append(p_line[p_line.index(',')+1:])
        s.append(s_line[p_line.index(',')+1:])
    else:
        p = [concatwords(p_line).split(' ')]
        s = [concatwords(s_line).split(' ')]
    return p, s


def splity(p_line,s_line):
    # if p_line[:p_line.index('y')].count('o') > 0 or p_line[:p_line.index('y')].count('d')>0:
    # why ['l', 'l'] ?
    if p_line.count('y') > 0 and p_line.index('y') > 0 and len(p_line) > p_line.index('y')+1 and \
            s_line[p_line.index('y')] == 'not' and p_line[p_line.index('y')+1] == 's' and p_line[p_line.index('y')+2] == ',':
        p = [p_line[:p_line.index('y')+2]]
        p.append(p_line[p_line.index('y')+2:])
        s = [s_line[:p_line.index('y') + 2]]
        s.append(s_line[p_line.index('y') + 2:])
    # elif p_line.count('y') > 0 and p_line.index('y') > 0 and p_line[:p_line.index('y')] != ['l','l']:
    elif p_line.count('y') > 0 and p_line.index('y') > 0:
        p = []
        s = []
        if p_line[:p_line.index('y')].count(',') > 0 and p_line[p_line.index('y')-1] != ',' \
                and p_line[:p_line.index('y')].count('s') == 1:
            temp_p, temp_s = splitshares(p_line[:p_line.index('y')], s_line[:p_line.index('y')])
        elif p_line[:p_line.index('y')].count(',') > 0 and p_line[p_line.index('y')-1] != ',':
            temp_p, temp_s = splitcom(p_line[:p_line.index('y')], s_line[:p_line.index('y')])
        elif p_line[:p_line.index('y')].count('and') > 0 and p_line[:p_line.index('y')].count('in') == 0:
            temp_p, temp_s = splitandc(p_line[:p_line.index('y')], s_line[:p_line.index('y')], 'and')
        elif p_line[:p_line.index('y')].count('or') > 0:
            temp_p, temp_s = splitandc(p_line[:p_line.index('y')], s_line[:p_line.index('y')], 'or')
        else:
            temp_p = [p_line[:p_line.index('y')]]
            temp_s = [s_line[:p_line.index('y')]]
        p.extend(temp_p)
        s.extend(temp_s)
        if p_line[p_line.index('y'):].count(',') > 0 and p_line[p_line.index('y'):].count('y') > 1 and \
                p_line[p_line.index('y'):][:2] == ['y','y'] and p_line[p_line.index('y')+2:].count('y') > 1:
            temp_index = p_line[p_line.index('y') + 2:].index('y') + p_line.index('y') + 2
            p_temp = []
            s_temp = []
            p_temp.append(p_line[p_line.index('y'):temp_index])
            s_temp.append(s_line[p_line.index('y'):temp_index])
            if p_line[temp_index+1:].count('y') > 0:
                temp_yy = temp_index + p_line[temp_index+1:].index('y') + 1
                p_temp.append(p_line[temp_index:temp_yy])
                p_temp.append(p_line[temp_yy:])
                s_temp.append(s_line[temp_index:temp_yy])
                s_temp.append(s_line[temp_yy:])
            else:
                p_temp.append(p_line[temp_index:])
                s_temp.append(s_line[temp_index:])
        elif p_line[p_line.index('y'):].count(',') > 0 and p_line[p_line.index('y') + p_line[p_line.index('y'):].\
                index(','):].count('y') > 0 and s_line.count('suspicious') == 0 and p_line[p_line.index('y'):][:2] != ['y','y']:
            p_temp, s_temp = partyc(p_line[p_line.index('y'):], s_line[p_line.index('y'):])
        elif p_line[p_line.index('y'):].count('or') > 0 and p_line[p_line.index('y'):].count(',') > 0 and\
                p_line[p_line.index('y'):].count('y') == 2 and p_line[p_line.index('y'):][:2] == ['y','y']:
            p_temp, s_temp = splitsharey(p_line[p_line.index('y'):], s_line[p_line.index('y'):], ',')
        elif p_line[p_line.index('y'):].count(',') == 0 and p_line[p_line.index('y'):].count('or') == 0 and \
                p_line[p_line.index('y'):].count('y') == 2 and p_line[p_line.index('y'):][:2] == ['y', 'y']:
            p_temp = [p_line[p_line.index('y'):]]
            s_temp = [s_line[p_line.index('y'):]]
        elif p_line[p_line.index('y')+1:].count('y') > 0:
            temp_index = p_line[p_line.index('y')+1:].index('y') + p_line.index('y')+1
            p_temp = []
            s_temp = []
            p_temp.append(p_line[p_line.index('y'):temp_index])
            s_temp.append(s_line[p_line.index('y'):temp_index])
            if len(p_line) > temp_index+1 and p_line[temp_index+1] == 'y' and p_line[temp_index+2:].count('y') > 0:
                index_yy = temp_index + p_line[temp_index + 2:].index('y') + 2
                p_share = [p_line[temp_index:index_yy]]
                p_share.append(p_line[index_yy:])
                s_share = [s_line[temp_index:index_yy]]
                s_share.append(s_line[index_yy:])
            elif p_line[temp_index+1:].count('y') > 0:
                index_yy = temp_index + p_line[temp_index+1:].index('y') + 1
                p_share = [p_line[temp_index:index_yy]]
                p_share.append(p_line[index_yy:])
                s_share = [s_line[temp_index:index_yy]]
                s_share.append(s_line[index_yy:])
            elif s_line[temp_index:].count('or') > 0:
                p_share, s_share = splitsharey(p_line[temp_index:], s_line[temp_index:], 'or')
            else:
                p_share, s_share = splitsharey(p_line[temp_index:], s_line[temp_index:], 'and')
            p_temp.extend(p_share)
            s_temp.extend(s_share)
        elif p_line[p_line.index('y'):].count('or') > 0:
            p_temp, s_temp = splitsharey(p_line[p_line.index('y'):], s_line[p_line.index('y'):], 'or')
        elif p_line[p_line.index('y'):].count('and') > 0:
            p_temp, s_temp = splitsharey(p_line[p_line.index('y'):], s_line[p_line.index('y'):], 'and')
        elif p_line[p_line.index('y'):].count(',') > 0:
            p_temp, s_temp = splitsharey(p_line[p_line.index('y'):], s_line[p_line.index('y'):], ',')
        else:
            p_temp, s_temp = splitmidy(p_line[p_line.index('y'):], s_line[p_line.index('y'):], 2)
        p.extend(p_temp)
        s.extend(s_temp)
    else:
        p = [concatwords(p_line).split(' ')]
        s = [concatwords(s_line).split(' ')]
    return p, s


def splitshared(p_line, s_line):
    if p_line.count(',') > 0 and p_line[p_line.index(','):].count('s') > 0 and len(set(p_line[p_line.index(','):])) \
            == 2 and p_line[:p_line.index(',')].count('d') > 0:
        p = []
        s = []
        p.append(p_line[:p_line.index(',')])
        s.append(s_line[:p_line.index(',')])
        temp_p = ['d']
        temp_p.extend(p_line[p_line.index(',') + 1:])
        p.append(temp_p)
        temp_s = [s_line[p_line.index('d')]]
        temp_s.extend(s_line[p_line.index(',') + 1:])
        s.append(temp_s)
    # elif p_line.count(',') > 0 and p_line[p_line.index(','):].count('s') > 0 and len(set(p_line[p_line.index(','):])) \
    #         == 2 and p_line[:p_line.index(',')].count('o') > 0:
    #     p = []
    #     s = []
    #     p.append(p_line[:p_line.index(',')])
    #     s.append(s_line[:p_line.index(',')])
    #     o_index = []
    #     temp_p = []
    #     temp_s = []
    #     for i in range(p_line.index(',')):
    #         if p_line[i] == 'o':
    #             o_index.append(i)
    #             temp_p.append(p_line[i])
    #     for i in o_index:
    #         temp_s.append(s_line[i])
    #     temp_p.extend(p_line[p_line.index(',') + 1:])
    #     p.append(temp_p)
    #     temp_s.extend(s_line[p_line.index(',') + 1:])
    #     s.append(temp_s)
    else:
        p = [concatwords(p_line).split(' ')]
        s = [concatwords(s_line).split(' ')]
    return p, s

def splitshares(p_line,s_line):
    if p_line.count(',') > 0 and p_line.count('s') == 1 and p_line[-1] == 's' and len(set(p_line))==3:
        p = []
        s = []
        if p_line[-2] != ',':
            temp_p = concatwords(p_line[:-1]).split(' , ')
            temp_s = concatwords(s_line[:-1]).split(' , ')
            for i in range(len(temp_p)):
                p.append((temp_p[i] + ' s').split())
                s.append((temp_s[i] + ' ' + s_line[-1]).split())
        elif p_line[-2] == ',':
            temp_p = concatwords(p_line).split(' , ')
            temp_s = concatwords(s_line).split(' , ')
            for i in range(len(temp_p)-1):
                p.append((temp_p[i] + ' s').split())
                s.append((temp_s[i] + ' ' + s_line[-1]).split())
    elif p_line.count(',') > 0 and p_line.count('s') == 1 and p_line[-1] == 's':
        p = []
        s = []
        temp_p = concatwords(p_line[:-1]).split(' , ')
        temp_s = concatwords(s_line[:-1]).split(' , ')
        t_p = []
        t_s = []
        for i in range(len(temp_p)):
            if temp_p[i].count(' and ') > 0:
                t_p.extend(temp_p[i].split(' and '))
                t_s.extend(temp_s[i].split(' and '))
            else:
                t_p.append(temp_p[i])
                t_s.append(temp_s[i])
        for j in range(len(t_p)):
            p.append((t_p[j] + ' s').split())
            s.append((t_s[j] + ' ' + s_line[-1]).split())
    elif p_line.count('and') > 0 and p_line.count('s') == 1 and len(set(p_line))==3 and p_line.index('s')<p_line.index('and'):
            # and p_line[:p_line.index('and')].count('o')>0 and p_line[p_line.index('and'):].count('o')>0:
        p = []
        s = []
        p.append(p_line[:p_line.index('and')])
        s.append(s_line[:s_line.index('and')])
        p.append((p_line[p_line.index('s')] + ' ' + concatwords(p_line[p_line.index('and')+1:])).split(' '))
        s.append((s_line[p_line.index('s')] + ' ' + concatwords(s_line[s_line.index('and')+1:])).split(' '))
    elif p_line.count('and') > 0 and p_line.count('s') == 1 and len(set(p_line))==3 and p_line.index('s') > p_line.index('and'):
        p = []
        s = []
        p.append((concatwords(p_line[:p_line.index('and')]) + ' ' + p_line[p_line.index('s')]).split(' '))
        s.append((concatwords(s_line[:s_line.index('and')]) + ' ' + s_line[p_line.index('s')]).split(' '))
        p.append(p_line[p_line.index('and') + 1:])
        s.append(s_line[s_line.index('and') + 1:])
    elif p_line.count('and') > 0 and p_line.count('s') == 1 and p_line[0] == 's' and p_line.count(',') > 0:
        # temp = [0]
        # temp_c = [i for i, v in enumerate(s_line) if v == ',']
        # temp.extend(temp_c)
        # temp.append(len(p_line))
        p = []
        s = []
        # for i in range(len(temp)-1):
        #     if i == 0:
        #         p.append(p_line[temp[i]:temp[i+1]])
        #         s.append(s_line[temp[i]:temp[i+1]])
        #     else:
        #         p.append((p_line[p_line.index('s')] + ' ' + concatwords(p_line[temp[i]:temp[i+1]])).split(' '))
        #         s.append((s_line[p_line.index('s')] + ' ' + concatwords(s_line[temp[i]:temp[i + 1]])).split(' '))
        temp_p = concatwords(p_line[1:]).split(' , ')
        for i in temp_p:
            if i.find('and') > -1:
                temp_i = i.split(' and ')
                for j in temp_i:
                    p.append((p_line[p_line.index('s')] + ' ' + j).split(' '))
            else:
                p.append((p_line[p_line.index('s')] + ' ' + i).split(' '))
        temp_s = concatwords(s_line[1:]).split(' , ')
        for i in temp_s:
            if i.find('and') > -1:
                temp_i = i.split(' and ')
                for j in temp_i:
                    s.append((s_line[p_line.index('s')] + ' ' + j).split(' '))
            else:
                s.append((s_line[p_line.index('s')] + ' ' + i).split(' '))
    else:
        p = [concatwords(p_line).split(' ')]
        s = [concatwords(s_line).split(' ')]
    return p, s


def splitcom(p_line, s_line):
    if p_line.count(',') > 0:
        # p = p_line.split(',')
        # s = s_line.split(',')
        # for i in p:
        #     if i.count('o') == 0 and i.count('d') == 0
        index_c = [0]
        temp = [i for i, v in enumerate(s_line) if v == ',']
        index_c.extend(temp)
        index_c.append(len(p_line))
        p = []
        s = []
        remove_i = []
        have_o = []
        for i in range(len(index_c)-1):
            if p_line[index_c[i]:index_c[i+1]].count('o') == 0 and p_line[index_c[i]:index_c[i+1]].count('d') == 0:
                if i == 0:
                    remove_i.append(index_c[i+1])
                elif have_o == []:
                    remove_i.append(index_c[i + 1])
                else:
                    remove_i.append(index_c[i])
            else:
                have_o.append(index_c[i+1])
        for j in remove_i:
            index_c.remove(j)
        for i in range(len(index_c) - 1):
            p.append(p_line[index_c[i]:index_c[i+1]])
            s.append(s_line[index_c[i]:index_c[i+1]])
    else:
        p = [concatwords(p_line).split(' ')]
        s = [concatwords(s_line).split(' ')]
    return p, s


def splitandc(p_line, s_line, word):
    if p_line[0] != 'y' and p_line.count(word) > 0 and p_line[:p_line.index(word)].count('o')>0 and \
            p_line[p_line.index(word):].count('o')>0:
        p = []
        s = []
        p.append(concatwords(p_line[:p_line.index(word)]).split(' '))
        p.append(concatwords(p_line[p_line.index(word)+1:]).split(' '))
        s.append(concatwords(s_line[:s_line.index(word)]).split(' '))
        s.append(concatwords(s_line[s_line.index(word) + 1:]).split(' '))
    elif p_line[0] != 'y' and p_line.count(word)>0 and p_line[:p_line.index(word)].count('o') > 0 and p_line[p_line.index(word):].count('d')>0:
        p = []
        s = []
        p.append(concatwords(p_line[:p_line.index(word)]).split(' '))
        p.append(concatwords(p_line[p_line.index(word)+1:]).split(' '))
        s.append(concatwords(s_line[:s_line.index(word)]).split(' '))
        s.append(concatwords(s_line[s_line.index(word) + 1:]).split(' '))
    elif p_line[0] != 'y' and p_line.count(word)>0 and p_line[:p_line.index(word)].count('d')>0 and p_line[p_line.index(word):].count('o')>0:
        p = []
        s = []
        p.append(concatwords(p_line[:p_line.index(word)]).split(' '))
        p.append(concatwords(p_line[p_line.index(word)+1:]).split(' '))
        s.append(concatwords(s_line[:s_line.index(word)]).split(' '))
        s.append(concatwords(s_line[s_line.index(word) + 1:]).split(' '))
    elif p_line[0] != 'y' and p_line.count(word) > 0 and p_line[:p_line.index(word)].count('d')>0 and p_line[p_line.index(word):].count('d')>0:
        p = []
        s = []
        p.append(concatwords(p_line[:p_line.index(word)]).split(' '))
        p.append(concatwords(p_line[p_line.index(word)+1:]).split(' '))
        s.append(concatwords(s_line[:s_line.index(word)]).split(' '))
        s.append(concatwords(s_line[s_line.index(word) + 1:]).split(' '))
    else:
        p = [concatwords(p_line).split(' ')]
        s = [concatwords(s_line).split(' ')]
    return p, s


def splitand(p_line, s_line, word):
    p = []
    s = []
    p_temp, s_temp = splitandc(p_line, s_line, word)
    for i in range(len(p_temp)):
        if p_temp[i].count('and') > 0:
            pp_temp, ss_temp = splitandc(p_temp[i], s_temp[i], word)
            p.extend(pp_temp)
            s.extend(ss_temp)
        else:
            p.append(p_temp[i])
            s.append(s_temp[i])
    return p, s


def uniqsp(s,p):
    uniq_s = list(set(s))
    new_p = []
    for i in uniq_s:
        new_p.append(p[s.index(i)])
    return uniq_s, new_p


noise = ['and', ',', 'or', 'in']

def deletenoise(s_line, p_line):
    while len(s_line) > 0 and noise.count(s_line[-1]) > 0:
        s_line = s_line[:-1]
        p_line = p_line[:-1]
    while len(s_line) > 0 and noise.count(s_line[0]) > 0:
        s_line = s_line[1:]
        p_line = p_line[1:]
    return s_line, p_line


# rlcp = ['right larger than left', 'right greater than left', 'right worse than left', 'left greater than right', \
#         'left worse than right']
# def findrlcp(s_line):
#     if s_line.count('right') > 0:
#         index_r = [i for i,v in enumerate(s_line) if v=='right']
#         for i in index_r:
#             if rlcp.count(concatwords(s_line[i:i+4])) > 0:
#                 return i, 1
#     elif s_line.count('left') > 0:
#         index_l = [i for i, v in enumerate(s_line) if v == 'left']
#         for i in index_l:
#             if rlcp.count(concatwords(s_line[i:i + 4])) > 0:
#                 return i, 1
#     else:
#         return 0, 0

def findrlcp(s_line):
    if s_line.count('right') > 0 and s_line[s_line.index('right'):s_line.index('right')+4] == ['right', 'larger', 'than', 'left']:
        return s_line.index('right'), 1
    elif s_line.count('right') > 0 and s_line[s_line.index('right'):s_line.index('right')+4] == ['right', 'greater', 'than', 'left']:
        return s_line.index('right'), 1
    elif s_line.count('right') > 0 and s_line[s_line.index('right'):s_line.index('right')+4] == ['right', 'worse', 'than', 'left']:
        return s_line.index('right'), 1
    elif s_line.count('left') > 0 and s_line[s_line.index('left'):s_line.index('left')+4] == ['left', 'greater', 'than', 'right']:
        return s_line.index('left'), 1
    elif s_line.count('left') > 0 and s_line[s_line.index('left'):s_line.index('left')+4] == ['left', 'worse', 'than', 'right']:
        return s_line.index('left'), 1
    elif s_line.count('greater') > 0 and s_line[s_line.index('greater')+1] == 'right':
        return s_line.index('greater'), 1
    elif len(s_line) > 2 and s_line[-2] == 'left' and s_line[-1] == 'small':
        return -2, 1
    else:
        return 0, 0


def findrl(s_line):
    s_index = []
    index_rl, eval = findrlcp(s_line)
    if eval == 1 and s_line[index_rl] == 'greater':
        s_index.append(index_rl)
        s_index.append(index_rl + 1)
    elif eval == 1 and s_line[index_rl:] == ['left','small']:
        s_index.append(index_rl)
        s_index.append(index_rl + 1)
    elif eval == 1:
        s_index.append(index_rl)
        s_index.append(index_rl + 1)
        s_index.append(index_rl + 2)
        s_index.append(index_rl + 3)
    return s_index


def newps(p_lines,s_lines):
    while p_lines.count('') > 0:
        p_lines.remove('')
    while s_lines.count('') > 0:
        s_lines.remove('')
    while s_lines.count([]) > 0:
        s_lines.remove([])
    return p_lines, s_lines

def rlstatus(p_line, s_line):
    answer = []
    key = []
    question = []
    q_num = 0
    if p_line[-4:] == '.txt' or p_line == '':
        answer.append(p_line)
        question.append(p_line)
        key.append(p_line)
    else:
        s_index = findrl(s_line)
        temp_s = []
        temp_p = []
        if s_index != []:
            for j in s_index:
                temp_s.append(s_line[j])
                temp_p.append(p_line[j])
            s_line = concatwords(s_line).replace(concatwords(temp_s), '').split()
            p_line = p_line.replace(concatwords(temp_p).replace(' ',''),'')
            s_line, p_line = deletenoise(s_line, p_line)
            q_element = concatwords(s_line)
            if q_element != '':
                answer.append(concatwords(temp_s))
                key.append(q_element)
                question.append('What is the comparision of ' + q_element + '?')
                q_num += 1
    return answer, key, question, q_num, p_line, s_line

def yes_how(p_line, s_line):
    answer = []
    key = []
    question = []
    q_num = 0
    if p_line[-4:] == '.txt' or p_line == '':
        question.append(p_line)
        key.append(p_line)
        answer.append(p_line)
    elif p_line.count('y') > 0 and p_line[0] != 'y' and p_line.index('y') > 0 and len(p_line) > p_line.index('y') + 1 \
            and p_line[p_line.index('y')+1] == 's':
        y_index = []
        temp_y = []
        temp_y_p = []
        y_index.append(p_line.index('y'))
        y_index.append(p_line.index('y')+1)
        if y_index != []:
            for j in y_index:
                temp_y.append(s_line[j])
                temp_y_p.append(p_line[j])
            s_line = concatwords(s_line).replace(concatwords(temp_y), '').split()
            p_line = p_line.replace(concatwords(temp_y_p).replace(' ', ''), '')
            s_line, p_line = deletenoise(s_line[:y_index[0]], p_line[:y_index[0]])
            q_element = concatwords(s_line)
            if q_element != '':
                answer.append(concatwords(temp_y))
                key.append(q_element)
                question.append('How is ' + q_element + '?')
                q_num += 1
                p_line = ''
                s_line = ''
    return answer,key,question,q_num,p_line,s_line


yes = ['with', 'represents', 'represent', 'representing', 'reflect', 'reflects', 'reflecting', 'causing','secondary']
def yes_no(p_line, s_line):
    answer = []
    key = []
    question = []
    q_num = 0
    if p_line[-4:] == '.txt' or p_line == '':
        answer.append(p_line)
        question.append(p_line)
        key.append(p_line)
    elif p_line == 'd' or p_line == 'od' or p_line == 'do' or p_line == 'ddo' or p_line == 'ood' or p_line == 'dpd':
        answer.append('yes')
        key.append(concatwords(s_line))
        question.append('Is there ' + concatwords(s_line) + '?')
        q_num += 1
        p_line = ''
        s_line = ''
    else:
        y_index = []
        temp_y = []
        temp_yp = []
        if p_line.count('yy') > 0:
            y_index.append(p_line.index('yy'))
            y_index.append(p_line.index('yy') + 1)
        elif p_line.count('y') > 0:
            y_index.append(p_line.index('y'))
        if y_index != []:
            for j in y_index:
                temp_y.append(s_line[j])
                temp_yp.append(p_line[j])
            for i in temp_y:
                s_line.remove(i)
            # s_line = concatwords(s_line).replace(concatwords(temp_y), '').split()
            p_line = p_line.replace(concatwords(temp_yp).replace(' ', ''), '')
            if len(temp_y) == 1 and yes.count(temp_y[0]) > 0:
                temp_y = 'yes'
            elif len(temp_y) == 2 and yes.count(temp_y[0]) > 0 and yes.count(temp_y[1]) > 0:
                temp_y = 'yes'
            if temp_y == 'yes':
                temp_s = []
                temp_p = []
                l_index = []
                temp_l = []
                temp_lp = []
                s_index = findrl(s_line)
                if s_index != []:
                    for j in s_index:
                        temp_s.append(s_line[j])
                        temp_p.append(p_line[j])
                    s_line = concatwords(s_line).replace(concatwords(temp_s), '').split()
                    p_line = p_line.replace(concatwords(temp_p).replace(' ', ''), '')
                    s_line, p_line = deletenoise(s_line, p_line)
                    q_element = concatwords(s_line)
                    if q_element != '':
                        answer.append(concatwords(temp_s))
                        key.append(q_element)
                        question.append('What is the comparision of ' + q_element + '?')
                        q_num += 1
                elif p_line.count('l') > 0 and p_line.count('d') > 0:
                    temp_d = []
                    if disease_prior.count(s_line[p_line.index('d')-1]) > 0:
                        temp_d.append(s_line[p_line.index('d')-1])
                    if len(p_line)> p_line.index('d')+1 and s_line[p_line.index('d')+1] == 'disease':
                        temp_d.append(s_line[p_line.index('d') + 1])
                    temp_d.append(s_line[p_line.index('d')])
                    for n in range(p_line.index('l'), len(p_line)):
                        if p_line[n] != 'd' and p_line[n] != 's' and disease_prior.count(s_line[n]) == 0:
                            l_index.append(n)
                    for n in l_index:
                        temp_l.append(s_line[n])
                        temp_lp.append(p_line[n])
                    s_line = concatwords(s_line).replace(concatwords(temp_s), '').split()
                    p_line = p_line.replace(concatwords(temp_lp).replace(' ', ''), '')
                    answer.append(concatwords(temp_l))
                    key.append(concatwords(temp_d))
                    question.append('Where is ' + concatwords(temp_d) + '?')
                    q_num += 1
                s_line, p_line = deletenoise(s_line, p_line)
                q_element = concatwords(s_line)
                if q_element != '':
                    answer.append(temp_y)
                    key.append(q_element)
                    question.append('Is there ' + q_element + '?')
                    q_num += 1
                    p_line = ''
                    s_line = ''
            elif concatwords(s_line) != '':
                s_line, p_line = deletenoise(s_line, p_line)
                q_element = concatwords(s_line)
                temp_y = concatwords(temp_y)
                answer.append(temp_y)
                key.append(q_element)
                question.append('Is there ' + q_element + '?')
                q_num += 1
                p_line = ''
                s_line = ''
    return answer, key, question, q_num, p_line, s_line


def inwhere(p_line, s_line):
    answer = []
    key = []
    question = []
    q_num = 0
    if p_line[-4:] == '.txt' or p_line == '':
        question.append(p_line)
        key.append(p_line)
        answer.append(p_line)
    else:
        temp_in = []
        temp_in_p = []
        if p_line.count('i') > 0 and p_line[p_line.index('i'):].count('d') == 0:
            in_index = list(range(p_line.index('i'), len(p_line)))
            s_index = []
            temp_s = []
            temp_sp = []
            if p_line[-2:] == ['s', 's']:
                s_index.append(in_index[-2])
                s_index.append(in_index[-1])
                in_index.remove(in_index[-2])
                in_index.remove(in_index[-1])
            if p_line[-1] == 's':
                s_index.append(in_index[-1])
                in_index.remove(in_index[-1])
            for j in in_index:
                temp_in.append(s_line[j])
                temp_in_p.append(p_line[j])
            for j in s_index:
                temp_s.append(s_line[j])
                temp_sp.append(p_line[j])
            if concatwords(temp_in) != 'in' and temp_in.count('size') == 0 and temp_in[1] != 'loss':
                # s_line = concatwords(s_line).replace(concatwords(temp_in), '').split()
                # for i in temp_s:
                #     s_line.remove(i)
                # p_line = p_line.replace(concatwords(temp_in_p).replace(' ', ''), '')
                # p_line = p_line.replace(concatwords(temp_sp).replace(' ', ''), '')
                s_line, p_line = deletenoise(s_line[:in_index[0]], p_line[:in_index[0]])
                q_element = concatwords(s_line)
                if q_element != '':
                    if p_line.count('d') > 0:
                        answer.append('yes')
                        key.append(q_element)
                        question.append('Is there ' + q_element + '?')
                        q_num += 1
                    if s_index != []:
                        answer.append(concatwords(temp_s))
                        key.append(q_element)
                        question.append('How is ' + q_element + '?')
                        q_num += 1
                    answer.append(concatwords(temp_in))
                    key.append(q_element)
                    question.append('Where is ' + q_element + '?')
                    q_num += 1
                    if p_line.count('s') == 0 and p_line.count('l') == 0:
                        p_line = ''
                        s_line = ''
        elif p_line.count('i') > 0 and p_line[p_line.index('i'):].count('d') > 0:
            d_index = p_line.index('d')
            d_name = s_line[d_index]
            s_line.remove(d_name)
            p_line = p_line.replace('d', '')
            s_line, p_line = deletenoise(s_line, p_line)
            a_element = concatwords(s_line)
            if a_element != '':
                answer.append('yes')
                key.append(d_name)
                question.append('Is there ' + d_name + '?')
                q_num += 1
                if a_element == 'increase in right and decrease in left basilar':
                    answer.append(a_element)
                    key.append(d_name)
                    question.append('Where is ' + d_name + '?')
                    q_num += 1
                elif a_element != 'in' and s_line.count('size') == 0:
                    s_index = []
                    temp_s = []
                    for n in range(len(p_line)):
                        if p_line[n] == 's':
                            s_index.append(n)
                    if s_index != []:
                        for n in s_index:
                            temp_s.append(s_line[n])
                    for n in temp_s:
                        s_line.remove(n)
                    p_line.replace('s', '')
                    s_line, p_line = deletenoise(s_line, p_line)
                    l_element = concatwords(s_line)
                    answer.append(l_element)
                    key.append(d_name)
                    question.append('Where is ' + d_name + '?')
                    q_num += 1
                    if temp_s != []:
                        answer.append(concatwords(temp_s))
                        key.append(d_name)
                        question.append('How is ' + d_name + '?')
                        q_num += 1
                elif a_element != 'in':
                    answer.append(a_element)
                    key.append(d_name)
                    question.append('How is ' + d_name + '?')
                    q_num += 1
                p_line = ''
                s_line = ''
    return answer,key,question,q_num,p_line,s_line

def findbugblank(p_lines, s_lines):
    for i in range(len(p_lines)):
        if p_lines[i] == '' and s_lines[i] != '':
            print('%d False' % i)
        elif p_lines[i] != '' and s_lines[i] == '':
            print('%d False' % i)


def limit_s(s_line):
    in_index = []
    if concatwords(s_line).count('upper limits normal or mildly enlarged') > 0:
        cur_index = s_line.index('upper')
        in_index.append(cur_index)
        in_index.append(cur_index + 1)
        in_index.append(cur_index + 2)
        in_index.append(cur_index + 3)
        in_index.append(cur_index + 4)
        in_index.append(cur_index + 5)
    elif concatwords(s_line).count('upper limits of normal and stable') > 0:
        cur_index = s_line.index('upper')
        in_index.append(cur_index)
        in_index.append(cur_index + 1)
        in_index.append(cur_index + 2)
        in_index.append(cur_index + 3)
        in_index.append(cur_index + 4)
        in_index.append(cur_index + 5)
    elif concatwords(s_line).count('upper limits normal or mildly enlarged') > 0:
        cur_index = s_line.index('upper')
        in_index.append(cur_index)
        in_index.append(cur_index + 1)
        in_index.append(cur_index + 2)
        in_index.append(cur_index + 3)
        in_index.append(cur_index + 4)
        in_index.append(cur_index + 5)
    elif concatwords(s_line).count('upper limits normal') > 0 or concatwords(s_line).count('upper limit normal') > 0:
        cur_index = s_line.index('upper')
        in_index.append(cur_index)
        in_index.append(cur_index + 1)
        in_index.append(cur_index + 2)
    elif concatwords(s_line).count('top limits normal') > 0 or concatwords(s_line).count('top normal limits') > 0:
        cur_index = s_line.index('top')
        in_index.append(cur_index)
        in_index.append(cur_index + 1)
        in_index.append(cur_index + 2)
    elif concatwords(s_line).count('upper normal stable') > 0:
        cur_index = s_line.index('upper')
        in_index.append(cur_index)
        in_index.append(cur_index + 1)
        in_index.append(cur_index + 2)
    elif concatwords(s_line).count('slightly upper normal') > 0:
        cur_index = s_line.index('slightly')
        in_index.append(cur_index)
        in_index.append(cur_index + 1)
        in_index.append(cur_index + 2)
    elif concatwords(s_line).count('top normal') > 0:
        cur_index = s_line.index('top')
        in_index.append(cur_index)
        in_index.append(cur_index + 1)
    elif concatwords(s_line).count('upper normal') > 0:
        cur_index = s_line.index('upper')
        in_index.append(cur_index)
        in_index.append(cur_index + 1)
    elif concatwords(s_line).count('normal limits') > 0:
        cur_index = s_line.index('normal')
        in_index.append(cur_index)
        in_index.append(cur_index + 1)
    return in_index


def upperlimit(p_line, s_line):
    answer = []
    key = []
    question = []
    q_num = 0
    if p_line[-4:] == '.txt' or p_line == '':
        question.append(p_line)
        key.append(p_line)
        answer.append(p_line)
    else:
        temp_in = []
        temp_in_p = []
        in_index = limit_s(s_line)
        if in_index != []:
            for j in in_index:
                temp_in.append(s_line[j])
                temp_in_p.append(p_line[j])
            s_line = concatwords(s_line).replace(concatwords(temp_in), '').split()
            p_line = p_line.replace(concatwords(temp_in_p).replace(' ', ''), '')
            s_line, p_line = deletenoise(s_line, p_line)
            q_element = concatwords(s_line)
            if q_element != '':
                answer.append(concatwords(temp_in))
                key.append(q_element)
                question.append('How is ' + q_element + '?')
                q_num += 1
                p_line = ''
                s_line = ''
    return answer, key, question, q_num, p_line, s_line


def within(p_line, s_line):
    answer = []
    key = []
    question = []
    q_num = 0
    if p_line[-4:] == '.txt' or p_line == '':
        question.append(p_line)
        key.append(p_line)
        answer.append(p_line)
    else:
        in_index = []
        temp_in = []
        temp_in_p = []
        if p_line.count('w') > 0:
            cur_index = p_line.index('w')
            in_index.append(cur_index)
            for m in p_line[cur_index + 1:]:
                if m != 'd' or m != 'y':
                    cur_index += 1
                    in_index.append(cur_index)
        if in_index != []:
            for j in in_index:
                temp_in.append(s_line[j])
                temp_in_p.append(p_line[j])
            s_line = concatwords(s_line).replace(concatwords(temp_in), '').split()
            p_line = p_line.replace(concatwords(temp_in_p).replace(' ',''),'')
            s_line, p_line = deletenoise(s_line[:in_index[0]],p_line[:in_index[0]])
            q_element = concatwords(s_line)
            if q_element != '':
                answer.append(concatwords(temp_in))
                key.append(q_element)
                if temp_in_p.count('l') > 0 or temp_in_p == ['w','o'] or temp_in_p == ['w','o','o']:
                    question.append('Where is ' + q_element + '?')
                else:
                    question.append('How is ' + q_element + '?')
                q_num += 1
                if p_line.count('s') == 0 and p_line.count('l') == 0:
                    p_line = ''
                    s_line = ''
    return answer, key, question, q_num, p_line, s_line


def onlystatus(p_line, s_line):
    answer = []
    key = []
    question = []
    q_num = 0
    if p_line[-4:] == '.txt' or p_line == '':
        question.append(p_line)
        key.append(p_line)
        answer.append(p_line)
    else:
        temp = list(set(p_line))
        if temp.count('s') > 0 and temp.count('l') == 0:
            s_index = []
            temp_s = []
            temp_sp = []
            for i in range(len(p_line)):
                if p_line[i] != 'o' and p_line[i] != 'd':
                    s_index.append(i)
            for j in s_index:
                temp_s.append(s_line[j])
                temp_sp.append(p_line[j])
            for j in temp_s:
                s_line.remove(j)
            for j in list(set(temp_sp)):
                p_line = p_line.replace('j', '')
            s_line, p_line = deletenoise(s_line, p_line)
            q_element = concatwords(s_line)
            if q_element != '':
                answer.append(concatwords(temp_s))
                key.append(q_element)
                question.append('How is ' + q_element +'?')
                q_num += 1
            p_line = ''
            s_line = ''
    return answer, key, question, q_num, p_line, s_line




disease_prior = ['airspace', 'disc', 'interstitial', 'pleural']

def slq(p_line, s_line):
    answer = []
    key = []
    question = []
    q_num = 0
    if p_line[-4:] == '.txt' or p_line == '':
        question.append(p_line)
        key.append(p_line)
        answer.append(p_line)
    else:
        s_index = []
        temp_s = []
        temp_sp = []
        l_index = []
        temp_l = []
        temp_lp = []
        o_index = -1
        # if p_line.count('sss') == 1 and p_line.count('sps') == 0 and p_line.replace('sss', '').count('s') == 0 \
        #         and p_line.count('d') > 0:
        if p_line.count('sss') == 1 and p_line.count('d') > 0:
            s_index.append(p_line.index('sss'))
            s_index.append(p_line.index('sss') + 1)
            s_index.append(p_line.index('sss') + 2)
            o_index = p_line.index('d')
        elif p_line.count('sps') == 1 and p_line.count('d') > 0:
            s_index.append(p_line.index('sps'))
            s_index.append(p_line.index('sps') + 1)
            s_index.append(p_line.index('sps') + 2)
            o_index = p_line.index('d')
        elif p_line.count('sss') == 1 and p_line.count('o') > 0:
            s_index.append(p_line.index('sss'))
            s_index.append(p_line.index('sss') + 1)
            s_index.append(p_line.index('sss') + 2)
            o_index = p_line.index('o')
        elif p_line.count('sps') == 1 and p_line.count('o') > 0:
            s_index.append(p_line.index('sps'))
            s_index.append(p_line.index('sps') + 1)
            s_index.append(p_line.index('sps') + 2)
            o_index = p_line.index('o')
        elif p_line.count('ss') == 1 and p_line.count('d') > 0:
            s_index.append(p_line.index('ss'))
            s_index.append(p_line.index('ss') + 1)
            o_index = p_line.index('d')
        elif p_line.count('ss') == 1 and p_line.count('o') > 0:
            s_index.append(p_line.index('ss'))
            s_index.append(p_line.index('ss') + 1)
            o_index = p_line.index('o')
        elif p_line.count('s') == 1 and p_line.count('d') > 0:
            s_index.append(p_line.index('s'))
            o_index = p_line.index('d')
        elif p_line[0] == 's' and p_line.count('d') > 0:
            s_index.append(0)
            o_index = p_line.index('d')
        elif p_line.count('s') == 1 and p_line.count('o') > 0:
            s_index.append(p_line.index('s'))
            o_index = p_line.index('o')
        elif p_line[0] == 's' and p_line.count('o') > 0:
            s_index.append(0)
            o_index = p_line.index('o')
        if o_index > -1 and p_line[o_index] == 'o':
            if p_line.count('sloo') > 0:
                l_index.append(p_line.index('l'))
            elif p_line.count('l') > 0:
                if p_line.index('l') < o_index:
                    l_index = list(range(p_line.index('l'), o_index))
                elif p_line.index('l') > o_index:
                    l_index = list(range(p_line.index('l'), len(p_line)))
                # l_index = list(range(len(p_line)))
                # l_index.remove(o_index)
                # if s_line[o_index] == 'soft':
                #     l_index.remove(o_index+1)
                # if s_line[o_index] == 'hilar' and len(p_line) > o_index + 1 and p_line[o_index+1] == 'o':
                #     l_index.remove(o_index+1)
                # if s_line[o_index] == 'hilar' and len(p_line) > o_index + 2 and p_line[o_index+2] == 'lymph':
                #     l_index.remove(o_index+2)
                # if s_line[o_index] == 'lymph' and len(p_line) > o_index + 1 and s_line[o_index+1] == 'node':
                #     l_index.remove(o_index+1)
                # if s_line[o_index] == 'cardiac' and len(p_line) > o_index + 1 and s_line[o_index+1] == 'silhouette':
                #     l_index.remove(o_index+1)
                # if s_line[o_index] == 'spine' and len(p_line) > o_index + 1 and s_line[o_index+1] == 'fusion':
                #     l_index.remove(o_index+1)
                # if s_line[o_index] == 'spinal' and len(p_line) > o_index + 1 and s_line[o_index+1] == 'fusion':
                #     l_index.remove(o_index+1)
                # if s_line[o_index] == 'pleural' and len(p_line) > o_index + 1 and p_line[o_index+1] == 'o':
                #     l_index.remove(o_index + 1)
                # if len(p_line) > o_index + 1 and s_line[o_index+1] == 'abnormality':
                #     l_index.remove(o_index + 1)
                # if len(p_line) > o_index + 1 and s_line[o_index+1] == 'abnormalities':
                #     l_index.remove(o_index+1)
                # if len(p_line) > o_index + 1 and s_line[o_index+1] == 'deformity':
                #     l_index.remove(o_index + 1)
                # if s_line[o_index] == 'foreign' and len(p_line) > o_index + 1:
                #     l_index.remove(o_index+1)
                for n in s_index:
                    if l_index.count(n) > 0:
                        l_index.remove(n)
                for i in l_index:
                    if p_line[i] == 's' or s_line[i] == 'deformity':
                        l_index.remove(i)
                # for i in range(p_line.index('l'),len(p_line)):
                #     if p_line[i] == 'l':
                #         l_index.append(i)
            for j in s_index:
                temp_s.append(s_line[j])
                temp_sp.append(p_line[j])
            if l_index != []:
                for j in l_index:
                    temp_l.append(s_line[j])
                    temp_lp.append(p_line[j])
                for i in temp_l:
                    s_line.remove(i)
                # s_line = concatwords(s_line).replace(concatwords(temp_l), '').split()
                p_line = p_line.replace(concatwords(temp_lp).replace(' ', ''), '')
                s_line, p_line = deletenoise(s_line, p_line)
                q_element = concatwords(s_line)
                if q_element != '':
                    answer.append(concatwords(temp_l))
                    key.append(q_element)
                    question.append('Where is ' + q_element + '?')
                    q_num += 1
            s_line = concatwords(s_line).replace(concatwords(temp_s), '').split()
            p_line = p_line.replace(concatwords(temp_sp).replace(' ', ''), '')
            s_line, p_line = deletenoise(s_line, p_line)
            q_element = concatwords(s_line)
            if q_element != '':
                answer.append(concatwords(temp_s))
                key.append(q_element)
                question.append('How is ' + q_element + '?')
                q_num += 1
                p_line = ''
                s_line = ''
        elif o_index > -1 and p_line[o_index] == 'd':
            if p_line.count('l') > 0:
                l_index = list(range(len(p_line)))
                l_index.remove(o_index)
                if disease_prior.count(s_line[o_index-1]) > 0:
                    l_index.remove(o_index-1)
                if len(p_line) > o_index + 1 and p_line[o_index+1] == 'd':
                    l_index.remove(o_index+1)
                if len(p_line) > o_index + 1 and s_line[o_index+1] == 'change':
                    l_index.remove(o_index+1)
                if len(p_line) > o_index + 1 and s_line[o_index+1] == 'changes':
                    l_index.remove(o_index+1)
                if len(p_line) > o_index + 1 and s_line[o_index+1] == 'deformity':
                    l_index.remove(o_index+1)
                if len(p_line) > o_index + 1 and s_line[o_index+1] == 'deformities':
                    l_index.remove(o_index+1)
                if len(p_line) > o_index + 1 and s_line[o_index+1] == 'lesion':
                    l_index.remove(o_index+1)
                if len(p_line) > o_index + 2 and p_line[o_index+1] == 'p' and p_line[o_index+2] == 'd':
                    l_index.remove(o_index+1)
                    l_index.remove(o_index+2)
                for n in s_index:
                    l_index.remove(n)
                for i in l_index:
                    if p_line[i] == 's':
                        l_index.remove(i)
            for j in s_index:
                temp_s.append(s_line[j])
                temp_sp.append(p_line[j])
            if l_index != []:
                for j in l_index:
                    temp_l.append(s_line[j])
                    temp_lp.append(p_line[j])
                for i in temp_l:
                    s_line.remove(i)
                # s_line = concatwords(s_line).replace(concatwords(temp_l), '').split()
                p_line = p_line.replace(concatwords(temp_lp).replace(' ', ''), '')
                s_line, p_line = deletenoise(s_line, p_line)
                # q_element = concatwords(s_line)
                # if q_element != '':
                #     answer.append(concatwords(temp_l))
                #     key.append(q_element)
                #     question.append('Where is ' + q_element + '?')
                #     q_num += 1
            s_line = concatwords(s_line).replace(concatwords(temp_s), '').split()
            p_line = p_line.replace(concatwords(temp_sp).replace(' ', ''), '')
            s_line, p_line = deletenoise(s_line, p_line)
            q_element = concatwords(s_line)
            if q_element != '':
                answer.append(concatwords(temp_l))
                key.append(q_element)
                question.append('Where is ' + q_element + '?')
                q_num += 1
                answer.append(concatwords(temp_s))
                answer.append('yes')
                key.append(q_element)
                key.append(q_element)
                question.append('How is ' + q_element + '?')
                question.append('Is there ' + q_element + '?')
                q_num += 2
                p_line = ''
                s_line = ''
    return answer, key, question, q_num, p_line, s_line


# def slq_2(p_line, s_line):
#     answer = []
#     key = []
#     question = []
#     q_num = 0
#     if p_line[-4:] == '.txt' or p_line == '':
#         question.append(p_line)
#         key.append(p_line)
#         answer.append(p_line)
#     else:
#         s_index = []
#         temp_s = []
#         temp_sp = []
#         l_index = []
#         temp_l = []
#         temp_lp = []
#         o_index = -1
#         if p_line.count('ss') == 1 and p_line.count('sps') == 0 and p_line.replace('ss', '').count('s') == 0 \
#                 and p_line.count('d') > 0:
#             s_index.append(p_line.index('ss'))
#             s_index.append(p_line.index('ss') + 1)
#             o_index = p_line.index('d')
#         elif p_line.count('ss') == 1 and p_line.count('sps') == 0 and p_line.replace('ss', '').count('s') == 0 \
#                 and p_line.count('o') > 0:
#             s_index.append(p_line.index('ss'))
#             s_index.append(p_line.index('ss') + 1)
#             o_index = p_line.index('o')
#         elif p_line.count('s') == 1 and p_line.count('d') > 0:
#             s_index.append(p_line.index('s'))
#             o_index = p_line.index('d')
#         elif p_line.count('s') == 1 and p_line.count('o') > 0:
#             s_index.append(p_line.index('s'))
#             o_index = p_line.index('o')
#         if o_index > -1 and p_line[o_index] == 'o':
#             if p_line.count('sloo') > 0:
#                 l_index.append(p_line.index('l'))
#             elif p_line.count('l') > 0:
#                 l_index = list(range(len(p_line)))
#                 l_index.remove(o_index)
#                 if p_line[o_index] == 'soft':
#                     l_index.remove(o_index+1)
#                 if p_line[o_index] == 'foreign':
#                     l_index.remove(o_index+1)
#                 for n in s_index:
#                     l_index.remove(n)
#             if l_index != []:
#                 for j in l_index:
#                     temp_l.append(s_line[j])
#                     temp_lp.append(p_line[j])
#             for j in s_index:
#                 temp_s.append(s_line[j])
#                 temp_sp.append(p_line[j])
#             s_line = concatwords(s_line).replace(concatwords(temp_s), '').split()
#             p_line = p_line.replace(concatwords(temp_sp).replace(' ', ''), '')
#             # s_line, p_line = deletenoise(s_line, p_line)
#             q_element = concatwords(s_line)
#             if q_element != '':
#                 answer.append(concatwords(temp_s))
#                 key.append(q_element)
#                 question.append('How is ' + q_element + '?')
#                 q_num += 1
#             if l_index == []:
#                 p_line = ''
#                 s_line = ''
#             else:
#                 s_line = concatwords(s_line).replace(concatwords(temp_l), '').split()
#                 p_line = p_line.replace(concatwords(temp_lp).replace(' ', ''), '')
#                 s_line, p_line = deletenoise(s_line, p_line)
#                 q_element = concatwords(s_line)
#                 if q_element != '':
#                     answer.append(concatwords(temp_l))
#                     key.append(q_element)
#                     question.append('Where is ' + q_element + '?')
#                     q_num += 1
#                 p_line = ''
#                 s_line = ''
#         elif o_index > -1 and p_line[o_index] == 'd':
#             if p_line.count('l') > 0:
#                 l_index = list(range(len(p_line)))
#                 l_index.remove(o_index)
#                 for n in s_index:
#                     l_index.remove(n)
#                 for j in l_index:
#                     temp_l.append(s_line[j])
#                     temp_lp.append(p_line[j])
#             for j in s_index:
#                 temp_s.append(s_line[j])
#                 temp_sp.append(p_line[j])
#             s_line = concatwords(s_line).replace(concatwords(temp_s), '').split()
#             p_line = p_line.replace(concatwords(temp_sp).replace(' ', ''), '')
#             # s_line, p_line = deletenoise(s_line, p_line)
#             q_element = concatwords(s_line)
#             if q_element != '':
#                 answer.append(concatwords(temp_s))
#                 answer.append('yes')
#                 key.append(q_element)
#                 key.append(q_element)
#                 question.append('How is ' + q_element + '?')
#                 question.append('Is there ' + q_element + '?')
#                 q_num += 2
#             if l_index == []:
#                 p_line = ''
#                 s_line = ''
#             else:
#                 s_line = concatwords(s_line).replace(concatwords(temp_l), '').split()
#                 p_line = p_line.replace(concatwords(temp_lp).replace(' ', ''), '')
#                 s_line, p_line = deletenoise(s_line, p_line)
#                 q_element = concatwords(s_line)
#                 if q_element != '':
#                     answer.append(concatwords(temp_l))
#                     key.append(q_element)
#                     question.append('Where is ' + q_element + '?')
#                     q_num += 1
#                 p_line = ''
#                 s_line = ''
#     return answer, key, question, q_num, p_line, s_line


def remains(p_line, s_line):
    answer = []
    key = []
    question = []
    q_num = 0
    if p_line[-4:] == '.txt' or p_line == '':
        question.append(p_line)
        key.append(p_line)
        answer.append(p_line)
    else:
        o_index = []
        temp_o = []
        if p_line.count('ooo') == 1 and p_line.count('s') >0 and p_line.replace('o','').replace('s','').replace('p','') == '':
            o_index.append(p_line.index('ooo'))
            o_index.append(p_line.index('ooo') + 1)
            o_index.append(p_line.index('ooo') + 2)
        elif p_line.count('oo') == 1 and p_line.count('s') >0 and p_line.replace('o','').replace('s','').replace('p','') == '':
            o_index.append(p_line.index('oo'))
            o_index.append(p_line.index('oo') + 1)
        elif p_line.count('o') == 1 and p_line.count('s') >0 and p_line.replace('o','').replace('s','').replace('p','') == '':
            o_index.append(p_line.index('o'))
        if o_index != []:
            for j in o_index:
                temp_o.append(s_line[j])
            key.append(concatwords(temp_o))
            question.append('How is ' + concatwords(temp_o) + '?')
            s_line = concatwords(s_line).replace(concatwords(temp_o), '').split()
            answer.append(concatwords(s_line))
            q_num += 1
            p_line = ''
            s_line = ''
    return answer, key, question, q_num, p_line, s_line


def locationq(p_line, s_line):
    answer = []
    key = []
    question = []
    q_num = 0
    if p_line[-4:] == '.txt' or p_line == '':
        question.append(p_line)
        key.append(p_line)
        answer.append(p_line)
    else:
        l_index = []
        temp_l = []
        temp_lp = []
        if p_line.count('l') > 0 and p_line.count('d') > 0 and p_line.index('l') < p_line.index('d'):
            for n in range(p_line.index('d')):
                if p_line[n] == 'l':
                    l_index.append(n)
            for j in l_index:
                temp_l.append(s_line[j])
                temp_lp.append(p_line[j])
            for i in temp_l:
                s_line.remove(i)
            # s_line = concatwords(s_line).replace(concatwords(temp_l), '').split()
            p_line = p_line.replace(concatwords(temp_lp).replace(' ', ''), '')
            s_line, p_line = deletenoise(s_line, p_line)
            q_element = concatwords(s_line)
            if q_element != '':
                answer.append(concatwords(temp_l))
                answer.append('yes')
                key.append(q_element)
                key.append(q_element)
                question.append('Where is ' + q_element + '?')
                question.append('Is there ' + q_element + '?')
                q_num += 2
                p_line = ''
                s_line = ''
        elif p_line.count('l') > 0 and p_line.count('d') > 0 and p_line.index('d') < p_line.index('l'):
            # for n in range(p_line.index('d')+1, len(p_line)):
            for n in range(p_line.index('l'), len(p_line)):
                if p_line[n] == 'l' or p_line[n] == 'o':
                    l_index.append(n)
            for j in l_index:
                temp_l.append(s_line[j])
                temp_lp.append(p_line[j])
            for i in temp_l:
                s_line.remove(i)
            # s_line = concatwords(s_line).replace(concatwords(temp_l), '').split()
            p_line = p_line.replace(concatwords(temp_lp).replace(' ', ''), '')
            s_line, p_line = deletenoise(s_line, p_line)
            q_element = concatwords(s_line)
            if q_element != '':
                answer.append(concatwords(temp_l))
                answer.append('yes')
                key.append(q_element)
                key.append(q_element)
                question.append('Where is ' + q_element + '?')
                question.append('Is there ' + q_element + '?')
                q_num += 2
                p_line = ''
                s_line = ''
        elif p_line.count('l') == 1 and p_line[p_line.index('l'):].count('o') > 0:
            l_index.append(p_line.index('l'))
            if l_index != []:
                for j in l_index:
                    temp_l.append(s_line[j])
                s_line = concatwords(s_line).replace(concatwords(temp_l), '').split()
                p_line = p_line.replace(concatwords(temp_lp).replace(' ', ''), '')
                if concatwords(s_line) == 'lung volumes':
                    answer.append(concatwords(temp_l))
                    key.append(concatwords(s_line))
                    question.append('How is ' + concatwords(s_line) + '?')
                    q_num += 1
                    p_line = ''
                    s_line = ''
                else:
                    s_line, p_line = deletenoise(s_line, p_line)
                    q_element = concatwords(s_line)
                    answer.append(concatwords(temp_l))
                    key.append(q_element)
                    question.append('Where is ' + q_element + '?')
                    q_num += 1
                    p_line = ''
                    s_line = ''
        elif p_line == 'ollo':
            l_index.append(1)
            l_index.append(2)
            l_index.append(3)
            for j in l_index:
                temp_l.append(s_line[j])
            s_line = concatwords(s_line).replace(concatwords(temp_l), '').split()
            answer.append(concatwords(temp_l))
            key.append(concatwords(s_line))
            question.append('Where is ' + concatwords(s_line) + '?')
            q_num += 1
            p_line = ''
            s_line = ''
    return answer, key, question, q_num, p_line, s_line


def remainl(p_line, s_line):
    answer = []
    key = []
    question = []
    q_num = 0
    if p_line[-4:] == '.txt' or p_line == '':
        question.append(p_line)
        key.append(p_line)
        answer.append(p_line)
    else:
        l_index = []
        temp_l = []
        if p_line == 'oddo':
            l_index.append(0)
        elif p_line == 'loddo':
            l_index.append(0)
            l_index.append(1)
        if l_index != []:
            for j in l_index:
                temp_l.append(s_line[j])
            answer.append(concatwords(temp_l))
            answer.append('yes')
            s_line = concatwords(s_line).replace(concatwords(temp_l), '').split()
            key.append(concatwords(s_line))
            key.append(concatwords(s_line))
            question.append('Where is ' + concatwords(s_line) + '?')
            question.append('Is there ' + concatwords(s_line) + '?')
            q_num += 2
            p_line = ''
            s_line = ''
    return answer, key, question, q_num, p_line, s_line


q_where = ['Where is lung well-aerated?', 'Where is lung stable and clear?', 'Where is lung hyperexpanded?', 'Where is lung clear?']
def modifyq(question):
    if q_where.count(question) > 0:
        question = question.replace('Where is lung', 'Which lung is')
    elif question == 'Where is bony?':
        question = 'Where is bony overlap?'
    elif question.find('changes deformity') > -1:
        question = question.replace('changes deformity', 'deformity')
    elif question.find('pulmonary pulmonary') > -1:
        question = question.replace('pulmonary pulmonary', 'pulmonary')
    elif question.find('size size') > -1:
        question = question.replace('size size', 'size')
    elif question.find('lung lungs') > -1:
        question = question.replace('lung lungs', 'lung')
    elif question == 'Where is persistent small pleural effusions , right , small left?':
        question = 'Where is persistent small pleural effusions?'
    elif question == 'Is there persistent small pleural effusions , right , small left?':
        question = 'Is there persistent small pleural effusions?'
    # elif question == 'How is disease spine?':
    #     question = 'How is disease of spine?'
    elif question == 'How is line cardiac enlargement?':
        question = 'How is cardiac enlargement?'
    return question

def dealstable(question):
    if question.find(' and stable?') > -1:
        question = question.replace(' and stable?', '?')
    elif question.find(' , stable?') > -1:
        question = question.replace(' , stable?', '?')
    elif question.find(' both stable?') > -1:
        question = question.replace(' both stable?', '?')
    elif question.find(' in stable?') > -1:
        question = question
    elif question.find(' stable?') > -1:
        question = question.replace(' stable?', '?')
    return question


def modifya(answer):
    answer = answer.split(' ')
    if answer[-2:] == [',', ','] or answer[-2:] == [',', 'and'] or answer[-2:] == [',', 'etiology'] or \
            answer[-2:] == [',', 'stable'] or answer[-2:] == ['in', 'size'] or answer[-2:] == ['in', 'thickness'] \
            or answer[-2:] == ['in', 'in']:
        answer = answer[:-2]
    elif answer[:2] == ['in','in'] or answer[:2] == ['in','within']:
        answer.remove('in')
    elif answer[-1] == 'and' or answer[-1] == ',' or answer[-1] == 'or' or answer[-1] == 'both' or answer[-1] == 'than' \
            or answer[-1] == 'in':
        answer = answer[:-1]
    elif answer[0] == ',' or answer[0] == 'and' or answer[0] == 'deformity':
        answer = answer[1:]
    # elif answer[-1] == 'heart' and answer[-2] == 'lobe':
    #     answer = answer[:-1]
    elif answer == ['no','no'] or answer == ['with','no'] or answer == ['suggesting','no']:
        answer = ['no']
    # elif answer == ['upper','normal','stable']:
    #     answer = ['upper', 'normal', 'but', 'stable']
    elif answer == ['mildly', 'and', 'mild']:
        answer = ['mild']
    return concatwords(answer)


reco = ['lung', 'lungs', 'base', 'bases', 'costophrenic', 'sulcus', 'sinus', 'pleura', 'both', 'thoracic', \
        'spine', 'retrocardiac']
reclo = ['hilar', 'hilum', 'pleural', 'sinus', 'sinuses', 'hemithorax', 'heart']
recol = ['both']
recor = ['pleural', 'mediastinal','pericardial']
def reclocation(plist, slist):
    if plist.count('or') > 0 and recor.count(slist[plist.index('or')-1]) > 0 and recor.count(slist[plist.index('or')+1]) > 0:
        plist[plist.index('or')-1] = 'l'
        plist[plist.index('or') + 1] = 'l'
    elif plist.count('l') > 0:
        for i in range(plist.index('l'), len(slist)):
            if reclo.count(slist[i]) > 0:
                plist[i] = 'l'
    elif plist.count('l') > 0 and recol.count(slist[plist.index('l')-1]) > 0:
        plist[plist.index('l') - 1] = 'l'
    elif plist.count('s') > 0 and plist[plist.index('s')+1:] == ['o', 'o', 'o'] and \
            reco.count(slist[plist.index('s')+2]) > 0 and reco.count(slist[plist.index('s')+3]) > 0:
        plist[plist.index('s') + 2] = 'l'
        plist[plist.index('s') + 3] = 'l'
    elif plist.count('d') > 0 and slist.count('without') == 0 and slist.count('no') == 0 and slist.count('negative') == 0:
        for i in range(len(slist)):
            if reco.count(slist[i]) > 0:
                plist[i] = 'l'
    return plist, slist


reco_1 = ['prominence', 'enlargement']
def recstatus(plist, slist):
    for i in reco_1:
        if slist.count(i) > 0 and slist.index(i) > 0 and len(slist) > slist.index(i) + 1 and \
                plist[slist.index(i) -1] == 's' and plist[slist.index(i) +1] == 'o':
            plist[slist.index(i)] = 's'
    return plist, slist

def recs_2(plist, slist):
    if slist.count('size') > 0 and slist.index('size') > 0 and slist[slist.index('size') -1] == 'increased':
        plist[slist.index('size')-1] = 's'
    elif slist.count('size') > 0 and slist.index('size') > 1 and slist[slist.index('size') -1] == 'in' and \
            slist[slist.index('size')-2] == 'increase':
        plist[slist.index('size')-1] = 's'
        plist[slist.index('size')-2] = 's'
    elif slist.count('size') > 0 and slist.index('size') > 1 and slist[slist.index('size') -1] == 'in' and \
            slist[slist.index('size')-2] == 'decrease':
        plist[slist.index('size')-1] = 's'
        plist[slist.index('size')-2] = 's'
    return plist, slist
# question - answer to make structured reports

from utils import findrl, limit_s, concatwords
import os

f1 = open('./results/simplified_reports.txt', 'r').read().splitlines()
f2 = open('./results/patterns.txt', 'r').read().splitlines()
s_q = open('./qg-statistics/select_questions.txt', 'r').read().splitlines()
target_dir = './qa/'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

from collections import defaultdict
simplified_reports = defaultdict(list)
coding = defaultdict(list)

temp = 'fake'
content = ''
for i in f1:
    if i[-4:] == '.txt':
        simplified_reports[temp].append(content)
        temp = i
        content = ''
    elif i[-4:] != '.txt' and i != '':
        content = content + i + ' . '

simplified_reports[temp].append(content)
del simplified_reports['fake']

temp = 'fake'
content = ''
for i in f2:
    if i[-4:] == '.txt':
        coding[temp].append(content)
        temp = i
        content = ''
    elif i[-4:] != '.txt' and i != '':
        content = content + i + ' . '

coding[temp].append(content)
del coding['fake']

keys = list(simplified_reports.keys())
# keys_2 = list(coding.keys())
# keys == keys_2


def find_key(q):
    temp = q.replace('?','').split()
    if temp[0] == 'What':
        key_words = concatwords(temp[5:])
    elif temp[0] == 'Which':
        key_words = temp[1] + ' ' + concatwords(temp[3:])
    else:
        key_words = concatwords(temp[2:])
    return key_words

neg = ['no', 'negative', 'none', 'not', 'cannot', 'without', 'exclude', 'excluded', 'clearing', 'cleared']
def no_neg(s, neg):
    num = 0
    for i in neg:
        if s.count(i) > 0:
            num += 1
    return num


def find_a(q, s, c):
    a_i = []
    if q.split()[0] == 'Is':
        if c.count('y') > 0:
            for i in range(len(c)):
                if c[i] == 'y':
                    a_i.append(i)
        else:
            a_i.append('yes')
    elif q.split()[0] == 'What':
        if findrl(s) != []:
            a_i = findrl(s)
    elif q.split()[0] == 'How' and no_neg(s, neg) == 0:
        if limit_s(s) != []:
            a_i = limit_s(s)
        elif c.count('within') > 0:
            a_i.append(c.index('within'))
            for i in range(c.index('within'), len(c)):
                if c[i] != 'd':
                    a_i.append(i)
        elif c.count('y') > 0 and len(c) > c.index('y')+1 and c[c.index('y')+1] == 's' and c[c.index('y'):].count('d') == 0:
            a_i.append(c.index('y'))
            a_i.append(c.index('y')+1)
        else:
            for i in range(len(c)):
                if c[i] == 's':
                    a_i.append(i)
    elif q.split()[0] == 'Which' and no_neg(s, neg) == 0:
        for i in range(len(c)):
            if c[i] == 'l':
                a_i.append(i)
    elif q.split()[0] == 'Where' and no_neg(s, neg) == 0:
        if c.count('in') > 0:
            a_i.append(c.index('in'))
            for i in range(c.index('in'), len(c)):
                if c[i] != 'd':
                    a_i.append(i)
        elif c.count('within') > 0 and c[c.index('within'):].count('s') == 0:
            a_i.append(c.index('within'))
            for i in range(c.index('within'), len(c)):
                if c[i] != 'd':
                    a_i.append(i)
        # elif c.count('s') == 0 and c.count('y') == 0:
        #     for i in range(len(c)):
        #         if key_words.count(s[i]) == 0:
        #             a_i.append(i)
        else:
            for i in range(len(c)):
                if c[i] == 'l':
                    a_i.append(i)
    return a_i


questions = []
answers = []
for k in keys:
    # print(k)
    questions.append(k)
    answers.append(k)
    report = simplified_reports[k][0]
    code = coding[k][0]
    temp_q = []
    temp_a = []
    for q in s_q:
        # print(q)
        key_words = find_key(q)
        e = report.count(key_words)
        if e > 0:
            report_s = report.split(' . ')
            code_s = code.split(' . ')
            for s in range(len(report_s)):
                if report_s[s].count(key_words) > 0:
                    r_s = report_s[s].split()
                    c_s = code_s[s].split()
                    a_index = find_a(q, r_s, c_s)
                    a = []
                    # print("s:{}, a_index:{}".format(s, a_index))
                    if a_index == ['yes']:
                        a.append('yes')
                    elif a_index != []:
                        for i in a_index:
                            a.append(r_s[i])
                    a = concatwords(a)
                    if a != '':
                        if temp_q.count(q) == 0:
                            temp_q.append(q)
                            temp_a.append(a)
                        elif temp_q.count(q) > 0 and temp_a[temp_q.index(q)] != a:
                            temp_q.append(q)
                            temp_a.append(a)
    questions.extend(temp_q)
    answers.extend(temp_a)
    questions.append('')
    answers.append('')


f = open(target_dir + 'qa_questions.txt','w')
for i in questions:
    f.write("%s\n" % i)

f.close()

f = open(target_dir + 'qa_answers.txt','w')
for i in answers:
    f.write("%s\n" % i)

f.close()

nr_q = 0
for i in questions:
    if i[-4:] != '.txt' and i != '':
        nr_q += 1

print('number of questions: ', nr_q)



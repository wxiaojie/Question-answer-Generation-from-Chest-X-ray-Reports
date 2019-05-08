all_answers = open('./results/all_answers.txt', 'r').read().splitlines()
all_questions = open('./results/all_questions.txt', 'r').read().splitlines()

import random

import os
# randomly check report files:
# reports_files = os.listdir('../reports/')
# check_list = []
# for i in range(10):
#     check_list.append(random.randint(0, len(reports_files)))

# for i in check_list:
#     print(reports_files[i])

# CXR2919_IM-1321-3001.txt, CXR3230_IM-1527-1001.txt, CXR1634_IM-0414-3003.txt, CXR3211_IM-1517-1001-0002.txt
# CXR1342_IM-0221-2001.txt, CXR1483_IM-0313-2001.txt, CXR3435_IM-1662-1001.txt, CXR2791_IM-1225-3001.txt
# CXR2960_IM-1354-1001.txt, CXR1122_IM-0080-2001.txt,
# CXR338_IM-1628-1001.txt, CXR1446_IM-0288-1001.txt, CXR3118_IM-1466-2001.txt, CXR2202_IM-0811-1001.txt,
# CXR1683_IM-0449-2001.txt, CXR3771_IM-1890-1001.txt, CXR3630_IM-1798-4004.txt, CXR523_IM-2134-2001.txt,
# CXR1109_IM-0076-2001.txt,

true_or_false = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
                 1, 1, 1, 1, 1, 1, 1, 1, 1, \

                 1, 1, 1, 1, 1, 1, 1, \
                 1, 1, 1, 1, 1, 1, 1, 1, \
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
                 1, 1, 1, 1, 1, 1, \

                 1, 1, 1, 1, 1, 1, \
                 1, 1, 1, 1, 1, 1, \

                 1, 1, 1, 1, 1, 1, 1, 1, \
                 1, 1, 1, 1, 1, 1, \
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
                 1, 1, \

                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, \
                 1, 0, 1, 1, \
                 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, \
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \

                 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 ]
q_type = ['Is', 'Is', 'Is', 'Is', 'Where', 'Is', 'Is', 'Is', 'How', 'How', 'How', \
          'Is', 'Is', 'Is', 'Is', 'How', 'Where', 'How', 'Is', 'How', 'Where', 'How', 'Is', 'How', \
          'Is', 'Is', 'Is', 'Is', 'Is', 'Is', 'Is', 'How', 'Where', 'How', 'How', 'How', 'Is', 'How', 'How', \
          'Is', 'Is', 'Is', 'Where', 'How', 'Is', 'How', 'How', 'How', \

          'Is', 'Is', 'Is', 'Is', 'Is', 'How', 'How', \
          'Is', 'Is', 'Is', 'Is', 'How', 'How', 'How', 'Where', \
          'Is', 'Is', 'Is', 'Is', 'Is', 'Is', 'Is', 'Where', 'How', 'How', 'How', \
          'Is', 'Is', 'Is', 'Is', 'How', 'How', \

          'Is', 'Is', 'Is', 'How', 'Where', 'How', \
          'Is', 'Is', 'Is', 'Is', 'How', 'How', \

          'Is', 'Is', 'Is', 'Is', 'Is', 'How', 'How', 'How', \
          'Is', 'Is', 'Is', 'Where', 'Is', 'How', \
          'Is', 'Is', 'Is', 'Is', 'Is', 'How', 'How', 'How', 'How', 'Is', \
          'How', 'How', \

          'Where', 'Is', 'How', 'What', 'Is', 'Is', 'Is', 'Is', 'Is', 'Is', 'Is', 'How', \
          'How', 'Where', 'How', 'How', \
          'Where', 'Where', 'Is', 'How', 'How', 'How', 'How', 'Is', 'Is', 'Is', \
          'Is', 'Is', 'Is', 'Is', 'Is', 'Is', 'Is', 'How', 'How', 'How', \

          'Is', 'Is', 'Is', 'Is', 'Is', 'How', 'How', 'How', 'How', \
          ]

qa_num = len(true_or_false)
qa_true = true_or_false.count(1)
print('Number of checked questions: ', qa_num) #163
print('Number of right answers: ', qa_true) #160
print('Number of right proportion: ', qa_true/float(qa_num)) #98.2%


qt_num = []
qt_num.append(q_type.count('Is'))
qt_num.append(q_type.count('How'))
qt_num.append(q_type.count('Where'))
qt_num.append(q_type.count('Which'))
qt_num.append(q_type.count('What'))
print('type of checked questions: ', qt_num)
# [91, 58, 13, 0, 1]


answers = []
questions = []
file_qa_num = []
temp_n = 0
for i in all_answers:
    if i[-4:] == '.txt':
        file_qa_num.append(temp_n)
        temp_n = 0
    elif i[-4:] != '.txt' and i != '':
        answers.append(i)
        temp_n += 1

file_qa_num.append(temp_n)
file_qa_num = file_qa_num[1:]

for i in all_questions:
    if i[-4:] != '.txt' and i != '':
        questions.append(i)

print('number of all_questions: ', len(questions))
# 63232
print('number of all_answers: ', len(answers))
# 63232

# q-a numbers in each report
all_n = sum(file_qa_num)  # 63232
average_n = all_n/float(len(file_qa_num))  # 8.5
from scipy.stats import mode
mode(file_qa_num) # 7
print('Sum, average, max, min, mode: ', all_n, average_n, max(file_qa_num), min(file_qa_num), mode)
# max = 30

uniq_q = list(set(questions))
uniq_a = list(set(answers))
print('number of uniq_questions: ', len(uniq_q))
# number of uniq_questions:  3532
print('number of uniq_anwsers: ', len(uniq_a))
# number of uniq_anwsers:  1293

#count Is there, how, where, which, what comparison
count_qtype = [0, 0, 0, 0, 0]
for i in questions:
    if i.split()[0] == 'Is':
        count_qtype[0] += 1
    elif i.split()[0] == 'How':
        count_qtype[1] += 1
    elif i.split()[0] == 'Where':
        count_qtype[2] += 1
    elif i.split()[0] == 'Which':
        count_qtype[3] += 1
    elif i.split()[0] == 'What':
        count_qtype[4] += 1

print('Number of each type of questions: ', count_qtype)
# [33012, 23196, 6820, 108, 96]
import numpy as np
print(np.asarray(count_qtype)/sum(count_qtype))
# [0.52207743 0.36683957 0.10785678 0.001708   0.00151822]

## calculate the frequency of questions
q_freq = []
q_c = []
for q in uniq_q:
    q_num = all_questions.count(q)
    q_c.append(q_num)
    q_freq.append((q_num, q))


uniq_qc = list(set(q_c))
q_c_freq = []
for i in uniq_qc:
    num = q_c.count(i)
    q_c_freq.append([i, num])

q_c_freq = np.asarray(q_c_freq)
print(sum(q_c_freq[:, 0] * q_c_freq[:, 1]))


q_c_freq = q_c_freq[q_c_freq[:, 0].argsort()]
temp = list(q_c_freq[:,0])
# new_x = list(range(len(uniq_qc)))
# new_x = np.c_[new_x, q_c_freq[:,0]]
for i in range(len(q_c)):
    q_c[i] = temp.index(q_c[i]) + 1

target_dir = './qg-statistics/'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)


a_freq = []
a_c = []
for a in uniq_a:
    a_num = all_answers.count(a)
    a_c.append(a_num)
    a_freq.append((a_num, a))

uniq_ac = list(set(a_c))
a_c_freq = []
for i in uniq_ac:
    num = a_c.count(i)
    a_c_freq.append([i, num])

a_c_freq = np.asarray(a_c_freq)
print(sum(a_c_freq[:, 0] * a_c_freq[:, 1]))

a_c_freq = a_c_freq[a_c_freq[:, 0].argsort()]
temp = list(a_c_freq[:,0])
for i in range(len(a_c)):
    a_c[i] = temp.index(a_c[i]) + 1


# answers (we focus on words), answers can be regarded as a multi-label classification, diverse combination of words
answer_words = []
for i in answers:
    temp = i.split()
    for j in temp:
        answer_words.append(j)

uniq_w = list(set(answer_words))
print('unique answer words: ', len(uniq_w)) # len(uniq_w) == 365
w_freq = []
w_c = []
for w in uniq_w:
    w_num = answer_words.count(w)
    w_c.append(w_num)
    w_freq.append((w_num, w))

uniq_wc = list(set(w_c))
w_c_freq = []
for i in uniq_wc:
    num = w_c.count(i)
    w_c_freq.append([i, num])

w_c_freq = np.asarray(w_c_freq)
# print(sum(w_c_freq[:, 0] * w_c_freq[:, 1]))


for i in range(len(q_c)):
    if q_c[i] > 7:
        q_c[i] = 8

for i in range(len(a_c)):
    if a_c[i] > 7:
        a_c[i] = 8

for i in range(len(w_c)):
    if w_c[i] > 7:
        w_c[i] = 8


select_qnum = q_c.count(8)
print('Selected questions: ', select_qnum) # 541
print('Proportion of selected questions: ', select_qnum/float(len(uniq_q)))
# 0.15317

select_anum = a_c.count(8)
print('Selected answers: ', select_anum) # 320
print('Proportion of selected answer-words: ', select_anum/float(len(uniq_a)))
# 0.24748

select_wnum = w_c.count(8)
print('Selected words: ', select_wnum) # 236
print('Proportion of selected answer-words: ', select_wnum/float(len(uniq_w)))
# 0.64657


f = open(target_dir + 'uniq_questions.txt','w')
for i in q_freq:
    f.write("%d " % i[0])
    f.write("%s\n" % i[1])


f.close()

f = open(target_dir + 'uniq_answers.txt','w')
for i in a_freq:
    f.write("%d " % i[0])
    f.write("%s\n" % i[1])


f.close()


f = open(target_dir + 'uniq_answerwords.txt','w')
for i in w_freq:
    f.write("%d " % i[0])
    f.write("%s\n" % i[1])


f.close()

# select_questions and select_words
f = open(target_dir + 'select_questions.txt','w')
for i in q_freq:
    if i[0] > 7:
        f.write("%s\n" % i[1])

f.close()

f = open(target_dir + 'select_words.txt','w')
for i in w_freq:
    if i[0] > 7 and i[1] != ',':
        f.write("%s\n" % i[1])

f.close()

# ground-truth questions and answers belonging to selected ones
select_q = open(target_dir + 'select_questions.txt', 'r').read().splitlines()

qa_gt_questions = []
qa_gt_answers = []
for i in range(len(all_questions)):
    if all_questions[i][-4:] == '.txt' or all_questions[i] == '' or select_q.count(all_questions[i]) > 0:
        qa_gt_questions.append(all_questions[i])
        qa_gt_answers.append(all_answers[i])

gt_num = 0
for i in all_questions:
    if select_q.count(i) > 0:
        gt_num += 1


print(gt_num) #55829
print('selected questions accounts for all the questions: ', gt_num/float(len(questions)))
# selected questions accounts for all the questions: 0.8829


f = open(target_dir + 'qa_gt_questions.txt','w')
for i in qa_gt_questions:
    f.write("%s\n" % i)

f.close()

f = open(target_dir + 'qa_gt_answers.txt','w')
for i in qa_gt_answers:
    f.write("%s\n" % i)

f.close()
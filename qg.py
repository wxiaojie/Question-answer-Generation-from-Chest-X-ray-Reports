from glob import glob
import os
from utils import concatwords, deletetail, deletehead,nood,nochange,negativefree,negativeclear,deleteand, extray
from utils import deleteor, deletecomma, gettemp, splitsharewithin, splityc, splitsharey, splitmidy, partyc, splitys
from utils import splitcom, splity, splitshares, splitandc, uniqsp, deletenoise, findrlcp, findrl, newps, yes_how
from utils import yes_no, inwhere, within, upperlimit, rlstatus, slq, remains, locationq, remainl, modifyq
from utils import splitand, changeinvolve, changesuperimpose, deletetails, dealstable, modifya, reclocation
from utils import recstatus, splitshared, onlystatus, recs_2

location = open('./keys/location.txt').read().splitlines()
status = open('./keys/status.txt').read().splitlines()
yes_or_no = open('./keys/yes_or_no.txt').read().splitlines()
object_names = open('./keys/object_names.txt').read().splitlines()
disease_names = open('./keys/disease_names.txt').read().splitlines()
prep = open('./keys/prep.txt').read().splitlines()
prep.append('.')
prep.append(',')
prep.append('involving')

attributes = location + status + yes_or_no
print(len(attributes) == len(set(attributes)))
a = set(attributes) | set(object_names)
print(len(attributes) + len(object_names) == len(a))
b = a | set(disease_names)
print(len(a) + len(disease_names) == len(b))


target_dir = './results/'
os.mkdir(target_dir)

reports_files = glob('./reports/*.txt')
print('number of reports_files: ', len(reports_files))

# delete those sentences with the following words:
dropwords = ['sacroiliac', 'hip', 'hips', 'knee', 'sacrum', 'metacarpal']
import re
num_pattern = re.compile(r'\d\.\d')

new_reports = []
pattern = []
for eachfile in reports_files:
    # print(eachfile.split('/')[-1])
    new_reports.append(eachfile.split('/')[-1])
    pattern.append(eachfile.split('/')[-1])
    contents = open(eachfile,'r').read()
    temp = num_pattern.findall(contents)
    if temp != []:
        for num in temp:
            contents = contents.replace(num, '')
    contents = contents.replace(', or ',' or ').replace(', and ',' and ').replace(' versus ',' and ').replace(' and/or ', ' and '). \
        replace('Low lung volumes, otherwise clear', 'Low lung volumes . Lungs are clear').\
        replace(',', ' , ').replace('.',' . ').replace(' knee: ', ' knee ').replace(':',' . ').replace(';', ' . ').\
        replace(' as well as ', ' and ').replace('differential diagnosis','differential').\
        replace('left worse right', 'left worse than right').replace(' other than ', ' . ').replace(' show ', ' . '). \
        replace(' shows ', ' . ').replace(' demonstrate ', ' . ').replace(' demonstrates ', ' . ').replace(' to suggest ', ' no ').\
        replace(' compatible with ', ' with ').replace(' compatible ', ' with ').\
        replace(' could be due to ', ' could ').replace(' may be due to ', ' may ').replace(' due to ', ' . ').\
        replace('may be related to', 'may').replace('possibly related to', 'possibly').replace('could be related to','could').\
        replace(' related to ', ' . ').replace('however', ' . ').replace(' filled nondilated', ' in').\
        replace('XXXX on the right', '').replace(' in XXXX opacities', '  opacities').replace(' relates to ', ' . ').\
        replace('mm in size', '').replace(' and associated ', ' . ').replace(' given ', ' . ').replace('allowing for', ' . ').\
        replace('and visualized upper abdomen', '').replace(' in normal limits', ' within normal limits').\
        replace('corresponding to', '.').lower().split(' ')
    temp_s = []
    temp_p = []
    for i in contents:
        if location.count(i) > 0:
            temp_s.append(i)
            temp_p.append('l')
        if status.count(i) > 0:
            temp_s.append(i)
            temp_p.append('s')
        if yes_or_no.count(i) > 0:
            temp_s.append(i)
            temp_p.append('y')
        elif object_names.count(i) > 0:
            temp_s.append(i)
            temp_p.append('o')
        elif disease_names.count(i) > 0:
            temp_s.append(i)
            temp_p.append('d')
        elif prep.count(i) > 0:
            temp_s.append(i)
            temp_p.append(i)
        elif dropwords.count(i) > 0:
            temp_s.append(i)
            temp_p.append('c')
    temp_p, temp_s = changeinvolve(temp_p, temp_s)
    temp_p, temp_s = changesuperimpose(temp_p, temp_s)
    temp_p = concatwords(temp_p).split('.')
    temp_s = concatwords(temp_s).split('.')
    drop_index = []
    drop_p = []
    drop_s = []
    for each_line in range(len(temp_p)):
        if temp_p[each_line].count('c') > 0:
            drop_index.append(each_line)
    if drop_index != []:
        for each_term in drop_index:
            drop_p.append(temp_p[each_term])
            drop_s.append(temp_s[each_term])
        for each_line in drop_p:
            temp_p.remove(each_line)
        for each_line in drop_s:
            temp_s.remove(each_line)
    while temp_p.count(' ') > 0:
        temp_p.remove(' ')
        temp_s.remove(' ')
    while temp_p.count('') > 0:
        temp_p.remove('')
        temp_s.remove('')
    temp_txtp = []
    temp_txts = []
    for j in range(len(temp_p)):
        # print(j)
        s_line = deletetail(temp_s[j].lstrip().rstrip().split(' '))
        p_line = temp_p[j].lstrip().rstrip().split(' ')[:len(s_line)]
        s_line = deletehead(s_line)
        p_line = p_line[len(p_line)-len(s_line):]
        p_line = nood(p_line)
        s_line = s_line[:len(p_line)]
        s_line, p_line = nochange(s_line, p_line)
        s_line, p_line = negativefree(s_line, p_line)
        s_line, p_line = negativeclear(s_line, p_line)
        s_line, p_line = deleteand(s_line, p_line)
        s_line, p_line = deleteor(s_line, p_line)
        s_line, p_line = deletecomma(s_line, p_line)
        p_line, s_line = reclocation(p_line, s_line)
        p_line, s_line = recstatus(p_line, s_line)
        if p_line.count('y') > 0 and p_line.index('y') > 0 and p_line[p_line.index('y'):].count('d') > 0:
            p, s = splity(p_line, s_line)
        elif p_line.count('y') > 0 and p_line.index('y') > 0 and p_line[p_line.index('y'):].count('o') > 0:
            p, s = splity(p_line, s_line)
        elif p_line.count('y') > 0 and p_line.index('y') > 0 and len(p_line) > p_line.index('y') + 1 \
                and p_line[p_line.index('y')+1] == 's' and p_line[p_line.index('y'):].count('l') == 0:
            p, s = splitys(p_line, s_line)
        elif p_line[2:].count('y') > 0:
            p, s = splitmidy(p_line, s_line,2)
        elif p_line.count('y') > 0 and p_line.index('y') == 0 and p_line.count('or') > 0:
            p, s = splitsharey(p_line, s_line,'or')
        elif p_line.count('y') > 0 and p_line.index('y') == 0:
            p, s = splitsharey(p_line, s_line, 'and')
        elif p_line.count('and') > 0 and p_line.count('within') > 0 and p_line.index('and') < p_line.index('within'):
            p, s = splitsharewithin(p_line, s_line)
        elif p_line.count('and') > 0 and p_line.count('within') > 0 and p_line.count(',') > 0 and \
                p_line.index('and') > p_line.index(',') > p_line.index('within'):
            p, s = splitsharewithin(p_line, s_line)
        elif p_line.count('and') > 0 and p_line.count('s') == 1 and len(set(p_line))==3:
            p, s = splitshares(p_line, s_line)
        elif p_line.count(',') > 0 and p_line.count('s') == 1 and len(set(p_line))==3:
            p, s = splitshares(p_line, s_line)
        elif p_line.count('and') > 0 and p_line.count('s') == 1 and len(set(p_line))==4 and p_line.count(',') > 0 \
                and p_line.count('o') > 0:
            p, s = splitshares(p_line, s_line)
        elif p_line.count(',') > 0 and p_line[p_line.index(','):].count('s') > 0 and \
                len(set(p_line[p_line.index(','):])) == 2 \
                and p_line[:p_line.index(',')].count('d') > 0:
            p, s = splitshared(p_line, s_line)
        elif p_line.count(',') > 0 and p_line.count('and') == 0:
            p, s = splitcom(p_line, s_line)
        elif p_line.count('and') > 1:
            p, s = splitand(p_line, s_line, 'and')
        elif p_line.count('and') == 1 and p_line[p_line.index('and') - 1] == p_line[p_line.index('and') + 1] == 's':
            p = [concatwords(p_line).split(' ')]
            s = [concatwords(s_line).split(' ')]
        elif p_line.count('and') == 1 and p_line[p_line.index('and') - 1] == p_line[p_line.index('and') + 1] == 'l':
            p = [concatwords(p_line).split(' ')]
            s = [concatwords(s_line).split(' ')]
        elif p_line != []:
            p, s = splitandc(p_line, s_line, 'and')
        else:
            p = []
            s = []
        for k in range(len(p)):
            p[k] = nood(deletehead(p[k]))
            s[k] = s[k][len(s[k]) - len(p[k]):]
            p[k] = deletetail(p[k])
            s[k] = s[k][:len(p[k])]
            s[k] = deletetails(s[k])
            p[k] = p[k][:len(s[k])]
            p[k], s[k] = extray(p[k], s[k])
            p[k], s[k] = reclocation(p[k], s[k])
            p[k], s[k] = recstatus(p[k], s[k])
            p[k], s[k] = recs_2(p[k], s[k])
            if len(p[k]) > 0 and p[k][0] != 'in':
                temp_txtp.append(concatwords(p[k]))
                temp_txts.append(concatwords(s[k]))
    uniq_s, uniq_p = uniqsp(temp_txts, temp_txtp)
    new_reports.append(uniq_s)
    pattern.append(uniq_p)


f1 = open(target_dir + 'simplified_reports.txt', 'w')
f2 = open(target_dir + 'patterns.txt', 'w')
for i in range(len(new_reports)):
    if new_reports[i][0] == 'C':
        f1.write("%s\n" % new_reports[i])
        f2.write("%s\n" % pattern[i])
    else:
        for j in range(len(new_reports[i])):
            if new_reports[i][j] != '' and new_reports[i][j] != ' ':
                f1.write('%s\n' % new_reports[i][j].lstrip().rstrip())
                f2.write('%s\n' % pattern[i][j].lstrip().rstrip())
        f1.write('\n')
        f2.write('\n')


f1.close()
f2.close()


## question - answer database    ------> find l/y/s, ask where/is there/how
def writefile(listname, filename, target_dir):
    f = open(target_dir + filename,'w')
    for i in listname:
        f.write('%s\n' % i)
    f.close()

tp_sentences_2 = open(target_dir + 'simplified_reports.txt', 'r').read().splitlines()
patterns = open(target_dir + 'patterns.txt', 'r').read().splitlines()

p_lines = []
s_lines = []
for j in range(len(patterns)):
    p_line = patterns[j]
    if p_line[-4:] == '.txt' or p_line == '':
        p_lines.append(p_line)
        s_lines.append(p_line)
    else:
        p_line = patterns[j].rstrip(',').replace('or', 'p').replace('and', 'p').replace('within','w').replace('in', 'i').split(' ')
        s_line = tp_sentences_2[j].rstrip(',').split(' ')
        p, s = splitandc(p_line, s_line, ',')
        for i in range(len(p)):
            s_line[i] = s_line[i].lstrip().rstrip().split(' ')
            p_lines.append(concatwords(p[i]).lstrip().rstrip().replace(' ', ''))
            s_lines.append(concatwords(s[i]).lstrip().rstrip().split(' '))


# print('length of p_lines: ', len(p_lines))   #71336


# for yes_how questions
question = []
key = []
answer = []
yhow_num = 0
for i in range(len(p_lines)):
    a, k, q, q_num, p_line, s_line = yes_how(p_lines[i], s_lines[i])
    answer.extend(a)
    key.extend(k)
    question.extend(q)
    yhow_num += q_num
    p_lines[i] = p_line
    s_lines[i] = s_line

print('Number of yeshow_questions: %d' % yhow_num)   # 27127

writefile(question,'yeshow_question.txt', target_dir)
writefile(key, 'yeshow_key.txt', target_dir)
writefile(answer, 'yeshow_answer.txt', target_dir)

p_lines, s_lines = newps(p_lines, s_lines)
# print(len(p_lines) == len(s_lines))    #44028


# for Is there questions
question = []
key = []
answer = []
yes_num = 0
for i in range(len(p_lines)):
    a, k, q, q_num, p_line, s_line = yes_no(p_lines[i], s_lines[i])
    answer.extend(a)
    key.extend(k)
    question.extend(q)
    yes_num += q_num
    p_lines[i] = p_line
    s_lines[i] = s_line

print('Number of yes_questions: %d' % yes_num)   # 27127

writefile(question,'yes_question.txt', target_dir)
writefile(key, 'yes_key.txt', target_dir)
writefile(answer, 'yes_answer.txt', target_dir)

p_lines, s_lines = newps(p_lines, s_lines)
# print(len(p_lines) == len(s_lines))    #44028

# for in_where questions
question = []
key = []
answer = []
in_num = 0

for i in range(len(p_lines)):
    # print(p_lines[i])
    a, k, q, q_num, p_line, s_line = inwhere(p_lines[i], s_lines[i])
    answer.extend(a)
    key.extend(k)
    question.extend(q)
    in_num += q_num
    p_lines[i] = p_line
    s_lines[i] = s_line

print('number of in_questions: %d' % in_num)   # 1343

writefile(question,'where_in_question.txt', target_dir)
writefile(key, 'where_in_key.txt', target_dir)
writefile(answer, 'where_in_answer.txt', target_dir)

p_lines, s_lines = newps(p_lines, s_lines)
# print(len(p_lines) == len(s_lines))  #43689


# for within_how questions
# some within followed by locations

question = []
key = []
answer = []
within_num = 0
for i in range(len(p_lines)):
    a, k, q, q_num, p_line, s_line = within(p_lines[i],s_lines[i])
    answer.extend(a)
    key.extend(k)
    question.extend(q)
    within_num += q_num
    p_lines[i] = p_line
    s_lines[i] = s_line

print('number of within_questions: %d' % within_num)   # 4442

writefile(question,'within_question.txt', target_dir)
writefile(key, 'within_key.txt', target_dir)
writefile(answer, 'within_answer.txt', target_dir)

p_lines, s_lines = newps(p_lines, s_lines)
# print(len(p_lines) == len(s_lines))  # 39490


# upper limits normal
question = []
key = []
answer = []
upper_num = 0
for i in range(len(p_lines)):
    a, k, q, q_num, p_line, s_line = upperlimit(p_lines[i],s_lines[i])
    answer.extend(a)
    key.extend(k)
    question.extend(q)
    upper_num += q_num
    p_lines[i] = p_line
    s_lines[i] = s_line

print('number of upper_questions: %d' % upper_num)   # 4442

writefile(question, 'upper_question.txt', target_dir)
writefile(key, 'upper_key.txt', target_dir)
writefile(answer, 'upper_answer.txt', target_dir)

p_lines, s_lines = newps(p_lines, s_lines)
# print(len(p_lines) == len(s_lines))  # 39490


# for special status questions: right larger/greater than left, left greater than right
question = []
key = []
answer = []
rls_num = 0
for i in range(len(p_lines)):
    a, k, q, q_num, p_line, s_line = rlstatus(p_lines[i],s_lines[i])
    answer.extend(a)
    key.extend(k)
    question.extend(q)
    rls_num += q_num
    p_lines[i] = p_line
    s_lines[i] = s_line

print('number of status_rl_questions: %d' % rls_num)

writefile(question,'status_rl_question.txt', target_dir)
writefile(key, 'status_rl_key.txt', target_dir)
writefile(answer, 'status_rl_answer.txt', target_dir)

p_lines, s_lines = newps(p_lines, s_lines)
# print(len(p_lines) == len(s_lines))  # 39490


# for status questions
question = []
key = []
answer = []
sl_num = 0
for i in range(len(p_lines)):
    # print(p_lines[i])
    a, k, q, q_num, p_line, s_line = slq(p_lines[i], s_lines[i])
    answer.extend(a)
    key.extend(k)
    question.extend(q)
    sl_num += q_num
    p_lines[i] = p_line
    s_lines[i] = s_line

print('Number of slq_questions: %d' % sl_num)   # 19276

writefile(question,'slq_question.txt', target_dir)
writefile(key, 'slq_key.txt', target_dir)
writefile(answer, 'slq_answer.txt', target_dir)

p_lines, s_lines = newps(p_lines, s_lines)
# print(len(p_lines) == len(s_lines))    #22025


# for another status questions
question = []
key = []
answer = []
status_num = 0
for i in range(len(p_lines)):
    a, k, q, q_num, p_line, s_line = remains(p_lines[i], s_lines[i])
    answer.extend(a)
    key.extend(k)
    question.extend(q)
    status_num += q_num
    p_lines[i] = p_line
    s_lines[i] = s_line


print('Number of status_questions: %d' % status_num)   # 708

writefile(question,'remains_question.txt', target_dir)
writefile(key, 'remains_key.txt', target_dir)
writefile(answer, 'remains_answer.txt', target_dir)

p_lines, s_lines = newps(p_lines, s_lines)
# print(len(p_lines) == len(s_lines))    #21317


# for location questions
question = []
key = []
answer = []
location_num = 0
for i in range(len(p_lines)):
    a, k, q, q_num, p_line, s_line = locationq(p_lines[i], s_lines[i])
    answer.extend(a)
    key.extend(k)
    question.extend(q)
    location_num += q_num
    p_lines[i] = p_line
    s_lines[i] = s_line

print('Number of location_questions: %d' % location_num)  #1946

writefile(question,'location_question.txt', target_dir)
writefile(key, 'location_key.txt', target_dir)
writefile(answer, 'location_answer.txt', target_dir)

p_lines, s_lines = newps(p_lines, s_lines)
# print(len(p_lines) == len(s_lines))   #20344


# for another location questions
question = []
key = []
answer = []
l_num = 0
for i in range(len(p_lines)):
    a, k, q, q_num, p_line, s_line = remainl(p_lines[i],s_lines[i])
    answer.extend(a)
    key.extend(k)
    question.extend(q)
    l_num += q_num
    p_lines[i] = p_line
    s_lines[i] = s_line

print('number of in_questions: %d' % l_num)   # 12

writefile(question,'remainl_question.txt', target_dir)
writefile(key, 'remainl_key.txt', target_dir)
writefile(answer, 'remainl_answer.txt', target_dir)

p_lines, s_lines = newps(p_lines, s_lines)
# print(len(p_lines) == len(s_lines))   # 19863

all_num = yhow_num + yes_num + in_num + within_num + upper_num + rls_num + sl_num + status_num + location_num + l_num
print('All original generated questions: ', all_num)


question_files = glob(target_dir + '*_question.txt')

example_q = open(question_files[0],'r').read().splitlines()
keys = [i for i in example_q if i[-4:] == '.txt']
len(keys)   #7430

from collections import defaultdict
questions = defaultdict(list)
answers = defaultdict(list)
dropquestion = ['Is there lung?', 'Where is lung?', 'Is there heart?', 'Is there chest?', 'Where is chest low?', \
                'Where is chest wall?', 'Where is chest?', 'Is there with chest?', 'Is there pulmonary?',\
                'Is there lung parenchyma?', 'Where is midline?', 'How is size?', \
                'Where is multiple thoracic?', 'Where is spinal?', 'Where is multiple vertebral?', 'Is there spinal?',\
                'Where is thorax?', 'Is there cardiothoracic?', 'Where is hemithorax?', \
                'How is limits?', 'Is there soft tissue?', 'Where is lung apices?',\
                'Is there numerous in posterior left pleural space?', 'Is there mediastinal?', \
                'Is there vascular structures?', 'Where is loss heart?', 'Is there increased size?', \
                'How is breast tissue lung bases?', 'How is capping?', 'Where is aneurysm?', 'Is there structures?']

dropanswer = ['hyper', 'side', 'or subsegmental atelectasis', '']

def refine(q_line):
    if q_line.count(', ,') > 0:
        q_line = q_line.replace(', ,', ',')
    elif q_line.count(', and and') > 0:
        q_line = q_line.replace(', and and', 'and')
    elif q_line.split(' ')[0] == 'Where' and q_line.split(' ')[-2:] == ['and', 'chest?']:
        q_line = concatwords(q_line.split(' ')[:-2]) + '?'
    elif q_line.split(' ')[0] == 'Is' and q_line.split(' ')[-2:] == ['and', 'chest?']:
        q_line = concatwords(q_line.split(' ')[:-2]) + '?'
    return q_line


for qfile in question_files:
    afile = target_dir + qfile.split('/')[-1][:-13] + '_answer.txt'
    temp_q = open(qfile,'r').read().splitlines()
    temp_a = open(afile,'r').read().splitlines()
    # len(temp_q) == len(temp_a)
    for i in range(len(temp_q)):
        if temp_q[i][-4:] == '.txt':
            temp_k = temp_q[i]
        elif temp_q[i] != '' and dropquestion.count(temp_q[i]) == 0 and dropanswer.count(temp_a[i]) == 0:
            q = refine(temp_q[i])
            q = dealstable(q)
            q = modifyq(q)
            a = modifya(temp_a[i])
            a = modifya(a)
            if q != '' and a != '':
                questions[temp_k].append(q)
                answers[temp_k].append(a)


f1 = open(target_dir + 'all_questions.txt','w')
f2 = open(target_dir + 'all_answers.txt', 'w')
for k in keys:
    f1.write('%s\n' % k)
    f2.write('%s\n' % k)
    temp_q = questions[k]
    temp_a = answers[k]
    for q in temp_q:
        f1.write('%s\n' % q)
    for a in temp_a:
        f2.write('%s\n' % a)
    f1.write('\n')
    f2.write('\n')

f1.close()
f2.close()

questions_num = 0
for k in keys:
    questions_num += len(questions[k])

print('Number of question_answer pairs after post-process: ', questions_num)  #62391


# change the turn of files in reports, to make it consistent with those in all_questions
reports = open('./reports.txt').read().splitlines()
f = open(target_dir + 'reports.txt','w')

for i in keys:
    f.write('%s\n' % i)
    temp = reports.index(i)
    for j in reports[temp+1:]:
        if j[-4:] == '.txt':
            break
        else:
            f.write('%s\n' % j)

f.close()

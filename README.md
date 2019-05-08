# Question-answer-Generation-from-Chest-X-ray-Reports

### Important files:
qg.py, statistics.py, qa.py, utils.py
reports.txt
keys, reports (directory)

1. question-answer generation according to pre-defined key words in directory keys
    python3 qg.py
    # this process first simplify the original reports
    # results are saved in a new directory: results
    # main results include: simplified_reports.txt, patterns (i.e., the coding files), all_answers.txt, and all_questions.txt
    # printed information:
        number of reports_files:  7430
        Number of yeshow_questions: 136
        Number of yes_questions: 28700
        number of in_questions: 2271
        number of within_questions: 4503
        number of upper_questions: 270
        number of status_rl_questions: 87
        Number of slq_questions: 26278
        Number of status_questions: 13
        Number of location_questions: 2948
        number of in_questions: 8
        All original generated questions:  65214
        Number of question_answer pairs after post-process:  63232


2. statistics on the above generated question-answer pairs
    python3 statistics.py
    # results are saved in a new directory: qg-statistics
    # main results include: select_questions.txt


3. question answering to augment the QA pairs
    python3 qa.py
    # results are saved in a new directory: qa
    # main results include: qa_answers.txt, qa_questions.txt

subject_each_score = 0
all_score_sum = 0
for i in range(20):
    subject, score, level = input().split()
    if level == 'A+':
        s = 4.5
    elif level == 'A0':
        s = 4.0
    elif level == 'B+':
        s = 3.5
    elif level == 'B0':
        s = 3.0
    elif level == 'C+':
        s = 2.5
    elif level == 'C0':
        s = 2.0
    elif level == 'D+':
        s = 1.5
    elif level == 'D0':
        s = 1.0
    elif level == 'F':
        s = 0.0
    else:
        continue
    subject_each_score += (float(score)*float(s))
    all_score_sum += float(score)
major_average = subject_each_score/all_score_sum
print(major_average)
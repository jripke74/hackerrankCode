if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
scores_queried_name = student_marks.get(query_name)
average_score = sum(scores_queried_name) / len(scores_queried_name)
print '%.2f' % (round(average_score, 2))

names_scores = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    temp_array = []
    temp_array.append(name)
    temp_array.append(score)
    names_scores.append(temp_array)
score_set = set()
for i in range(len(names_scores)):
    score_set.add(names_scores[i][1])
scores_sorted = sorted(score_set)
second_lowest = scores_sorted[1]
name_arr = []
for i in range(len(names_scores)):
    if second_lowest == names_scores[i][1]:
        name_arr.append(names_scores[i][0])
sorted_names = sorted(name_arr)
for i in range(len(sorted_names)):
    print sorted_names[i]

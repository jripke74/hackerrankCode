if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    num_set = set(arr)
    num_set_sorted = sorted(num_set)
    runner_up_score = num_set_sorted[-2]
    print(runner_up_score)

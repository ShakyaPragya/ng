def count_pos(arr):
    pos_count = 0
    neg_count = 0
    for num in arr:
        if num >= 0:
            pos_count += 1
        else:
            neg_count += 1
    print("Positive numbers count:", pos_count)
    print("Negative numbers count:", neg_count)

count_pos({1,-2,-3,4,-5})
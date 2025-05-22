def find_odd(arr):
    seen = set()
    for num in arr:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)
    for num in seen:
        return num

assert find_odd([20, 1, 1, 2, 2, 3, 3, 20, 4, 4, 5, 5, 99]) == 99

# n time/space

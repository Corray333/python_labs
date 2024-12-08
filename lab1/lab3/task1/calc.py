def count_pairs(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    N, K = map(int, lines[0].split())
    ratings = list(map(int, lines[1:]))
    
    ratings.sort()
    count = 0
    left = 0
    right = N - 1
    
    while left < right:
        if ratings[left] + ratings[right] >= K:
            count += (right - left)
            right -= 1
        else:
            left += 1
    
    return count

result_A = count_pairs('numbers.txt')

print(result_A)
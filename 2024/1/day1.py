
def count(left, right):
    total = 0
    left_s = sorted(left)
    right_s = sorted(right)

    for i in range(0, len(left_s)):
        total += abs(int(left_s[i]) - int(right_s[i]))

    return total

def similar(left, right):
    total = 0
    
    for i in range(0, len(left)):
        sim_score = right.count(left[i])
        total += sim_score * int(left[i])
    
    return total

f = open("input.txt")
left, right = [], []

for line in f.readlines():
    split = line.split()
    left.append(split[0])
    right.append(split[1])

print(count(left, right))
print(similar(left, right))
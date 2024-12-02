from helper import fileManager
file = fileManager('day1Input')
#file = fileManager('day1Sample1')
data = file.getRawData().split()
print(data)
left = []
right = []

for i, v in enumerate(data):
    if i%2 == 0:
        left.append(v)
    else:
        right.append(v)

for i in range(len(left)):
    print( left[i] + ' ' + right[i])

left.sort()
right.sort()

print('sorted')
def part1(left,right):
    sum = 0
    for i in range(len(left)):
        if left[i] >= right[i]:
                sum += int(left[i]) - int(right[i])
        else:
            sum += int(right[i]) - int(left[i])
        print( left[i] + ' ' + right[i])
    print(sum)
#part1(left,right)
def part2(left,right):
    sum = 0
    for item in left:
        countInRight = right.count(item)
        sum += int(item) * int(countInRight)
    print(sum)
part2(left,right)
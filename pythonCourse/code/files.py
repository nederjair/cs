def writeNums():
    nums = input('enter numbers: ')
    file = open('index.txt', 'w')
    for num in nums.split():
        file.write(num)
        file.write('\n')
    file.close()


file = open('index.txt', 'r')
lines = file.read()
print(lines)
file.close()

ints_nums = lines.split()
print(ints_nums)
#print(max(ints_nums))
#print(min(ints_nums))
#print(sum(ints_nums))

data = [1,3,6,2,5,4,9,8,7,10]
K = 3

def quick_select(begin, end, rank):
    left = 0
    right = len(data) - 1
    mid = left + int((right - left) / 2)

    while True:
        val = data[mid]
        # Swap the value to the first position
        data[left], data[mid] = data[mid], data[left]
        # Move the partition to the correct side
        swap_pos = left + 1
        for i in range(left+1, right+1):
            if data[i] < val:
                print('swap: ' + str(data[i]) + '<=>' + str(data[swap_pos]))
                data[i], data[swap_pos] = data[swap_pos], data[i]
                swap_pos = swap_pos + 1
            else:
                print('skip:' + str(data[i]))
        # Switch the data to the right position
        data[left], data[swap_pos] = data[swap_pos], data[left]
        break

print(data)
quick_select(0, len(data)-1, 5)
print(data)
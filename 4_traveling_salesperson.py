import sys

cost_matrix = [
    [0, 10, 15, 20],
    [5,  0,  9, 10],
    [6, 13,  0, 12],
    [8,  8,  9,  0],
]

target = 0

'''
S(target, 0, i) = cost_matrix[target, i] 
S(target, 1, i) = min_j(S(target, 1, j) + cost_matrix[j, i])
S(target, 2, i) = min_j(S(target, 2, j) + cost_matrix[j, i])
'''

temp = {}

# Base cases, from target to i
# M1->2, M1->3, M1->4
remainings = set([i for i in range(4)])
remainings.remove(target)
traveled = set()
for i in range(4):
    if i == target:
        continue
    remainings.remove(i)
    dist = cost_matrix[target][i]    
    temp[(frozenset(traveled), frozenset(remainings), i)] = dist
    remainings.add(i)
print(temp)

# Increment cases
for count in range(2): # Already had 2 add more 2 to get 1->(2,3)->4
    new_temp = {}
    for key in temp:
        traveled = set(key[0])
        remainings = set(key[1])
        dest = key[2]
        to_adds = remainings.copy()        
        print(' Extend: traveled = ' + str(traveled) + ', dest = ' + str(dest) + ', remainings = ' + str(remainings) + ', dist = ' + str(temp[key]))
        for to_add in to_adds:
            # Get next_stop, add to travel and check if we already calculated, skip if so 
            traveled.add(to_add)
            remainings.remove(to_add)            
            next_key = (frozenset(traveled), frozenset(remainings), dest)
            if next_key not in new_temp:
                print('  Calculating: traveled = ' + str(traveled) + ', dest = ' + str(dest) + ', remainings = ' + str(remainings))
                # Remove one from traveled to the dest and extend the path from there
                to_stops = traveled.copy()  
                min_dist = sys.maxsize
                for to_stop in to_stops:
                    traveled.remove(to_stop)
                    remainings.add(dest)
                    lookup_key = (frozenset(traveled), frozenset(remainings), to_stop)
                    add_dist = cost_matrix[to_stop][dest]
                    total_dist = temp[lookup_key] + add_dist
                    print('  Use: ' + str(lookup_key) + ' + ' + str(to_stop) + '->' + str(dest))
                    print('   Dist: ' + str(temp[lookup_key]) + ' + ' + str(add_dist) + '=' + str(total_dist))
                    if total_dist < min_dist:
                        min_dist = total_dist
                    remainings.remove(dest)
                    traveled.add(to_stop)
                new_temp[next_key] = min_dist
                print(' Save: ' + str(next_key) + ' => ' + str(min_dist))
            traveled.remove(to_add)
            remainings.add(to_add)
    print(new_temp)
    temp = new_temp

# Final state, back to target
min_dist = sys.maxsize
for key in temp:
    dest = key[2]
    dist = temp[key] + cost_matrix[dest][target]
    print(':: 0->' + str(key[0]) + '->' + str(dest) + '->0 = ' + str(dist))
    if dist < min_dist:
        min_dist = dist

print('Min Distance = ' + str(min_dist))
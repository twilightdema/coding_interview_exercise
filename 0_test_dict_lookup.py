NUM_OF_TEST = 1000000
NUM_OF_PROP = 5

from array import array
import random
import time

random_key_list = []
random_key_list_joined = []
random_key_list_int = []

MAX_KEY_VALUE = NUM_OF_PROP * NUM_OF_PROP

# Generate list of key to be added. Note that each test case will have the same 
# key values so the tests are fair.
for i in range(NUM_OF_TEST):
    key1 = int(random.random() * NUM_OF_PROP)
    key2 = int(random.random() * NUM_OF_PROP)
    random_key_list.append((str(key1), str(key2)))
    random_key_list_joined.append(str(key1) + ':' + str(key2))
    random_key_list_int.append(key1 * NUM_OF_PROP + key2)

def test_2_levels():
    data = {}
    for key1, key2 in random_key_list:
        if key1 not in data:
            data_level1 = {}
            data[key1] = data_level1
        else:
            data_level1 = data[key1]
        if key2 not in data_level1:
            data_level1[key2] = 1
        else:
            data_level1[key2] = data_level1[key2] + 1

def test_2_levels_with_get():
    data = {}
    for key1, key2 in random_key_list:
        data_level1 = data.get(key1, {})
        data_level1[key2] = data_level1.get(key2, 0) + 1

def test_1_level():
    data = {}
    for key in random_key_list_joined:
        if key not in data:
            data[key] = 1
        else:
            data[key] = data[key] + 1

def test_1_level_with_get():
    data = {}
    for key in random_key_list_joined:
        data[key] = data.get(key, 0) + 1

def test_1_level_fixed_array():
    data = [0 for _ in range(MAX_KEY_VALUE)]
    for key in random_key_list_int:
        data[key] = data[key] + 1


t0 = time.time()
test_2_levels()
t2 = time.time() - t0

t0 = time.time()
test_2_levels_with_get()
t2_get = time.time() - t0

t0 = time.time()
test_1_level()
t1 = time.time() - t0

t0 = time.time()
test_1_level_with_get()
t1_get = time.time() - t0

t0 = time.time()
test_1_level_fixed_array()
t3 = time.time() - t0

print('Time for 2 Levels = ' + str(t2))
print('Time for 2 Levels with Get = ' + str(t2_get))
print('Time for 1 Level = ' + str(t1))
print('Time for 1 Level with Get = ' + str(t1_get))
print('Time for 1 Level Fixed Size Array = ' + str(t3))

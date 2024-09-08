def common_elements():
    multiples_of_3 = set()
    for x in range(100):
        if x % 3 == 0:
            multiples_of_3.add(x)
    multiples_of_5 = set()
    for x in range(100):
        if x % 5 == 0:
            multiples_of_5.add(x)
    common_set = multiples_of_3.intersection(multiples_of_5)
    return common_set

# Тест
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, 'Test failed'

print('ОК')
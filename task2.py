nested_list1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

def flat_generator1(_list):
    for nested in _list:
        for nest in nested:
            yield nest

for item in  flat_generator1(nested_list1):
	print(item)
print('=' * 20)  
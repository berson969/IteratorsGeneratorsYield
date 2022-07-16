nested_list2 = [
    [[[[['X']]]]],
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None, ['new', 'old', ['more','one more']]],
    ['test']
]

def full_flat_generator1(_list, i=True, stack=[]):
    while i:
        for nest in _list:
            if isinstance(nest, list):
                _list.extend(nest)
                i = True
            else:
                stack.append(nest)
                i = False
    return stack

[print(x) for x in full_flat_generator1(nested_list2)]

# с YIELD лежит в main 4.2
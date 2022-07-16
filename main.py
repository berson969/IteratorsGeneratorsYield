# from itertools import chain

nested_list1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]
nested_list2 = [
    [[[[['X']]]]],
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None, ['new', 'old', ['more','one more']]],
    ['test']
]


print('Задание 1\n')
# с помощью двух обращений к классу
class FlatIterator:
    def __init__(self, _list):
        self._list = _list
    def __iter__(self):
        self.cursor = -1
        return self
    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self._list):
            raise StopIteration  
        return self._list[self.cursor]

for item in FlatIterator(nested_list1):
    if isinstance(item, list):
        [print(x) for x in FlatIterator(item)]
    else:
        print(item)
print('=' * 20)


print('Задание2.1\n')
# два вложенных for
def flat_generator1(_list):
    for nested in _list:
        for nest in nested:
            yield nest

for item in  flat_generator1(nested_list1):
	print(item)
print('=' * 20)  


print('Задание2.2\n')
from itertools import chain

def  flat_generator2(_list):
    return chain.from_iterable(_list)

for item in  flat_generator2(nested_list1):
	print(item)
print('=' * 20)


print('Задание 3\n')
class FullFlatIterator:
    def __init__(self, _list):
        self._list = _list
    def __iter__(self):
        self.stack = [iter(self._list)]#список из итераторов
        aaa = self.stack
        return self
    def __next__(self, i=True):
        while self.stack:
            try:
                nest = next(self.stack[-1]) #берем из последнего элемента в списке
                # print(nest)
            except StopIteration:
                self.stack.pop() #если итератор кончился удаляем его из стека
                continue
            if isinstance(nest, list):
                self.stack.append(iter(nest)) #один раз итератор развернутого списока снова записывается
            else:
                return nest
        raise StopIteration  
        

for item in FullFlatIterator(nested_list2):
    print(item)            
print('=' * 20)


print('Задание 4.1\n')
# распрямление с помощью extend
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
print('=' * 20)


print('Задание 4.2\n')
# обращение в функции к самой функции
def full_flat_generator2(_list):
    for nest in _list:
        if isinstance(nest, list):
            for nest_in_nest in full_flat_generator2(nest):
            # OR without 'continue'
            # yield from full_flat_generator2(nest)
                continue
        else:
            yield nest

for item in full_flat_generator2(nested_list2):
    print(item)            

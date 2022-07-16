nested_list2 = [
    [[[[['X']]]]],
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None, ['new', 'old', ['more','one more']]],
    ['test']
]

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
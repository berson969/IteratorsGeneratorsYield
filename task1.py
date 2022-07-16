nested_list1 = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

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
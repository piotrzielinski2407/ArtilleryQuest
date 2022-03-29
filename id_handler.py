from singleton_pattern import Singletone


class IdHandler(metaclass=Singletone):
    def __init__(self, *args, **kwargs):
        self.storage = {}
        self.next_index = 1

    def set_id(self, object_to_set):
        current_index = self.next_index
        if object_to_set not in self.storage:
            self.storage[current_index] = object_to_set
            self.next_index = self.__update_index()
            return current_index
        else:
            return self.__find_key(object_to_set)

    def unset_id(self, object_to_unset):
        if object_to_unset in self.storage:
            index_to_unset = self.__find_key(object_to_unset)
            self.storage.pop(index_to_unset)
            self.next_index = self.__update_index()

    def __find_key(self, object_to_find):
        value_index = list(self.storage.values()).index(object_to_find)
        index_to_return = list(self.storage.keys())[value_index]
        return index_to_return

    def __update_index(self):
        storage_len = len(self.storage)
        if storage_len == 0:
            return 1
        elif max(list(self.storage.keys())) == storage_len:
            return storage_len+1
        else:
            stored_keys_set = set(self.storage.keys())
            max_key_value = max(self.storage.keys())
            max_keys_set = set([i for i in range(1, max_key_value+1)])
            next_key = min(max_keys_set.difference(stored_keys_set))
            return next_key
# TODO tests


if __name__ == '__main__':
    class1 = IdHandler()
    class2 = IdHandler()
    print(id(class2), id(class2))

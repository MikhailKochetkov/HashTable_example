class HashTable:
    size = 20

    def __init__(self):
        self.data = [None] * self.size

    def __getitem__(self, key):
        h = self.get_hash(key)
        try:
            while self.data[h]:
                if self.data[h] and self.data[h]["key"] == key:
                    return self.data[h]
                h = self.get_rehash(h)
        except IndexError:
            return

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.data[h] is None or self.data[h]["key"] == 'deleted':
            self.data[h] = {"key": key, "value": value}
            return
        next_h = self.get_rehash(h)
        try:
            while self.data[next_h] is not None:
                if self.data[next_h]["key"] == key or self.data[next_h]["key"] == 'deleted':
                    self.data[next_h]["key"] = key
                    self.data[next_h]["value"] = value
                    return
                next_h = self.get_rehash(next_h)
        except IndexError:
            raise Exception("Не хватает места в таблице")
        self.data[next_h] = {"key": key, "value": value}

    def get_hash(self, name):
        return len(name) % self.size

    def get_rehash(self, oldhash):
        return oldhash + 1

    def delete(self, key):
        h = self.get_hash(key)
        try:
            if self.data[h]["key"] == key:
                self.data[h] = {"key": 'deleted', "value": 'deleted'}
                return
        except TypeError:
            raise Exception("Не существует элемента с таким ключом")
        h_next = self.get_rehash(h)
        try:
            while self.data[h_next] is not None:
                if self.data[h_next]["key"] == key:
                    self.data[h_next] = {"key": 'deleted', "value": 'deleted'}
                    return
                h_next = self.get_rehash(h_next)
        except IndexError:
            raise Exception("Не существует элемента с таким ключом")
        raise Exception("Не существует элемента с таким ключом")
        

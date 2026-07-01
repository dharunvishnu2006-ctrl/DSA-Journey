class HashMap:
    def __init__(self, size=4):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return

    def keys(self):
        keys_list = []
        for bucket in self.table:
            for key, value in bucket:
                keys_list.append(key)
        return keys_list
    
hm = HashMap()

hm.put("name", "Dharun")
hm.put("age", 20)
hm.put("city", "Coimbatore")    
print(hm.keys())
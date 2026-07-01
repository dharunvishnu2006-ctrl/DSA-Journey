class HashMap:
    def __init__(self, size=8):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.count += 1
        if self.count / self.size > 0.75:
            self._resize()

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)

    def get(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)
h3 = HashMap(size=2)
for i in range(10):
    h3.put(f"key{i}", i)
print("Size after growth:", h3.size)
print("Count:", h3.count)
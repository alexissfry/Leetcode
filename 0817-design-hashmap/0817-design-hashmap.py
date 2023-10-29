class Bucket:
    def __init__(self):
        self.bucket = []
    
    def get(self, key):
        for (k,v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False 
        for i,kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key,value))

    def remove(self, key):
        for i,kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
        
class MyHashMap:
    def __init__(self):
        self.keyLen = 2069
        self.hashTable = [Bucket() for i in range(self.keyLen)]

    def put(self, key: int, value: int) -> None:
        hashKey = key % self.keyLen
        self.hashTable[hashKey].update(key,value)

    def get(self, key: int) -> int:
        hashKey = key % self.keyLen
        return self.hashTable[hashKey].get(key)
        
    def remove(self, key: int) -> None:
        hashKey = key % self.keyLen
        self.hashTable[hashKey].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
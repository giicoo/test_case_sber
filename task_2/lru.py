from typing import Any, Dict, Hashable, List


class Cache:
    value: Any
    used_c: int

    def __init__(self, value: Any, used_c:int=1):
        self.value=value
        self.used_c=used_c
    
    def __repr__(self):
        return f"Cache(value={self.value}, used_c={self.used_c})"
    
    def __str__(self):
        return self.value
        

class LRUCache:
    cache: Dict[Hashable, Cache]
    capacity: int

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
    
    def get(self, key: Hashable):
        cache = self.cache.get(key)
        if not cache:
            return None
        cache.used_c+=1
        return cache
    
    def put(self, key: Hashable, value: Any):
        if not self.get(key):
            if len(self.cache)<self.capacity:
                self.cache[key]=Cache(value=value)
            else:
                min_c=100000
                del_k=None
                for k, v in self.cache.items():
                    if v.used_c<min_c:
                      del_k=k
                      min_c=v.used_c
                del self.cache[del_k]
                self.cache[key]=Cache(value=value)
        else:
            cache = self.get(key)
            self.cache[key]=Cache(value=value, used_c=cache.used_c)
            

    
    def __len__(self):
        return len(self.cache)

lru = LRUCache(2)
lru.put("124", "124")

lru.put("122", "122")
print(repr(lru.get("122")))

print(lru.cache)

lru.put(1222, "1222")
print(lru.get(1222))
lru.put(1222, "12222")

print(lru.cache)
print(len(lru))


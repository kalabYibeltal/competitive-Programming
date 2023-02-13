class AllOne:

    def __init__(self):
        self.key_count = defaultdict(int)
        self.count_key = defaultdict(set)
        self.max_heap = []
        self.min_heap = []
        

    def inc(self, key: str) -> None:
        original_value = self.key_count[key]
        if self.count_key[original_value]:
            self.count_key[original_value].remove(key)
        original_value+=1
        self.count_key[original_value].add(key)
        self.key_count[key]=original_value
        heapq.heappush(self.max_heap, -(original_value))
        heapq.heappush(self.min_heap, (original_value))   
        return
        

    def dec(self, key: str) -> None:
        original_value = self.key_count[key]
        self.count_key[original_value].remove(key)
        original_value -= 1
        if original_value == 0:
            del self.key_count[key]
            return
        
        self.count_key[original_value].add(key)
        self.key_count[key]=original_value
        heapq.heappush(self.max_heap, -(original_value))
        heapq.heappush(self.min_heap, (original_value)) 
        return

    def getMaxKey(self) -> str:
        if len(self.key_count) == 0:
            return ""
        
        while self.max_heap:
            val = -heapq.heappop(self.max_heap)
            if self.count_key[val]:
                heapq.heappush(self.max_heap, -val)
                for key in self.count_key[val]:
                    return key
        return
        

    def getMinKey(self) -> str:
        if len(self.key_count) == 0:
            return ""
        
        while self.min_heap:
            val = heapq.heappop(self.min_heap)
            if self.count_key[val]:
                heapq.heappush(self.min_heap, val)
                for key in self.count_key[val]:
                    return key
        return
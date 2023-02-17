class LRUCache:
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remaining = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        var = self.dic.pop(key) 
        self.dic[key] = var  
        return var

    def put(self, key, value):
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if self.remaining > 0:
                self.remaining -= 1  
            else:  # self.dic is full
                self.dic.popitem(last=False) 
        self.dic[key] = value
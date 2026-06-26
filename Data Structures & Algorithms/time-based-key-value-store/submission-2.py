class TimeMap:

    def __init__(self):
        self.hashMap = {} # str : list of pairs        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashMap:
            return ""

        keyList = self.hashMap[key]
        return self.binary_search(keyList, timestamp)
            
    def binary_search(self, keyList, target: int): 
        l, r = 0, len(keyList) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            if keyList[m][1] == target:
                return keyList[m][0]
            elif keyList[m][1] < target:
                res = keyList[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
    
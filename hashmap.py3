class HashMap:
    def __init__(self):
        self.map = []

    def getSize(self):
        print(f"HashMap size is {len(self.map)}.")
        return len(self.map)
    
    def items(self):
        return self.map

    def showItems(self):
        print("{")
        for pair in self.map:
            print(f"{pair}")
        print("}")

    def clearMap(self):
        print("HashMap Cleared.")
        self.map = []

    def areEqual(self, map):
        if self.getSize() != map.getSize():
            print("HashMaps are not equal.")
            return False
        for pair in self.map:
            if self.searchKey(pair[0]) != map.searchKey(pair[0]):
                print("HashMaps are not equal.")
                return False

        print("HashMaps are equal.")    
        return True

    def mergeMap(self, map):
        self.map = self.map + map.items()

    def storeKeyValue(self, key, value):
        item = []
        item.append(key)
        item.append(value)
        self.map.append(item)

    def deleteKeyValue(self, key):
        isFound = False

        for pair in self.map:
            if pair[0] == key:
                isFound = True
                print(f"Key value pair: [{key}: {pair[1]}] removed from HashMap.")
                self.map.remove(pair)

        if not isFound:
            print(f"Key: {key} does not exist in HashMap.")

    def searchKey(self, key):
        isFound = False

        for pair in self.map:
            if pair[0] == key:
                isFound = True
                print(f"Value: {pair[1]} for Key: {pair[0]}")
                return pair[1]
            
        if not isFound:
            print(f"Key: {key} does not exist in HashMap.")
            return -1

    def updateValue(self, key, value):
        isFound = False

        for pair in self.map:
            if pair[0] == key:
                isFound = True
                print(f"Value updated to {value} for Key: {key}.")
                pair[1] = value

        if not isFound:
            print(f"Key: {key} does not exist in HashMap.")


hmap = HashMap()
hmap.storeKeyValue("Matthew", 22)
hmap.storeKeyValue("Joshua", 20)
hmap.showItems()

hmap1 = HashMap()
hmap1.storeKeyValue("Paul", 53)
hmap1.storeKeyValue("Maggie", 49)
hmap1.showItems()

hmap.mergeMap(hmap1)
hmap.showItems()
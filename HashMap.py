# Hashmap => Insert some items into the space effectivly

"""
ITEM : Apple

for char in ITEN
convert char to key using a hashfunction

"""


class HashMap(object):


    def __init__(self):
        self.size = 10
        self.bucket = [None] * self.size
    

    def HashFunction(self,key):
        Hash = 0
        for char in key:
            Hash += ord(char)
        return Hash % self.size
    
    def Add(self, key, value):
        keyIndex = self.HashFunction(key)

        arr = [key, value]

        if self.bucket[keyIndex] is None:
            self.bucket[keyIndex] = list([arr])
            return True
        else:
            """['apple', 'Apple']
            """
            for pair in self.bucket[keyIndex]:
                if pair[0] == key:
                    pair[1] == value
                else:
                    pass
    
    def __setitem__(self, key, value):
        return self.Add(key, value)

    def Print(self):
        print(self.bucket)



if __name__ == "__main__":
    d = HashMap()
    d["name"] = "Danish"
    d["eman"] = "Sharma"
    d["n"] = "akhil"
    d.Print()

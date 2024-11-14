class LinkedList:
    def __init__(self, l):
        self.list = []
        self.rootp = -1
        self.freep = 0
        for i in range(l):
            self.list.append([None, i+1])
        self.list[l-1][1] = -1
        self.visualise()
    def visualise(self):
        i = 0
        while i < len(self.list):
            print(f"[{i}] {self.list[i][0]}\t{self.list[i][1]}\t{'<- root pointer' if self.rootp == i else ''}\t{'<- free pointer' if self.freep == i else ''}")
            i += 1
        print("=========")
    def insert(self, elem): 
        if self.freep == -1:
            print("Unable, not free!")
        self.list[self.freep][0] = elem 
        tmp = self.list[self.freep][1]
        self.list[self.freep][1] = self.rootp 
        self.rootp = self.freep
        self.freep = tmp
        #self.visualise()
new_list = LinkedList(10)
names = [
    "Steven",
    "Xi Jinping",
    "Deng Xiaoping",
    "Chiang Kai-shek",
    "Donald Trump"
]
for name in names:
    new_list.insert(name)
new_list.visualise()
"""names = []
ptrs = []
l = 10
for i in range(10):
    names.append(None)
    ptrs.append(i+1)
ptrs[9] = -1
sp = -1
fp = 0
print(names)
print(ptrs)
def insert_one(name):
    global sp
    global fp
    global ptrs
    global names
    if fp == -1:
        print("Not free")
        return
    names[fp] = name
    ptrs[fp] = sp
    sp = fp
    fp = ptrs[fp]
    print(names)
    print(ptrs)
insert_one("Steven")
insert_one("Steven2")"""

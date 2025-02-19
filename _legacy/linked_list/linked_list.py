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


import random
def generator(l, up, low, h):
    linked = []
    linkedp = []
    for i in range(l):
        linked.append(random.randint(up, low) if i < h else None)
        if i == h - 1:
            linkedp.append(-1)
            continue
        linkedp.append(i+1)
    return (linked, linkedp, 0, -1, h)
# my_list = [37, 18, 49, 77, 68, None, None, None, None, None]
# my_plist = [-1, 0, 1, 2, 3, 4, 5, 6, 7, -1]
def delete(element, my_list, my_plist, start, null, heap):
    #global start, heap, my_list, null
    if start == null:
        # empty
        print("Linked list empty")
        return None
    index = start
    oldIndex = start
    while my_list[index] != element and index != null:
        oldIndex = index
        index = my_plist[index]
    if index == null:
        print("Item does not exist.")
        return None
    tmp_pointer = my_plist[index]
    my_plist[index] = heap
    my_plist[oldIndex] = tmp_pointer
LENGTH = 15
l,p,s,n,h = generator(LENGTH, 0, 100, round(LENGTH / 2))
for i in range(len(l)):
    print(f"[{i}]\t{l[i]}\t{p[i]}\t{'<- heap' if i == h else ''}{'<- root' if i == s else ''}")
print("-------")
delete(int(input("$ ")), l, p, s, n, h)
for i in range(len(l)):
    print(f"[{i}]\t{l[i]}\t{p[i]}\t{'<- heap' if i == h else ''}{'<- root' if i == s else ''}")

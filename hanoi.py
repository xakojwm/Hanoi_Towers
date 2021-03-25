class disk:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class peg:
    def __init__(self,index):
        self.head = None
        self.tail = None
        self.length = 0
        self.index = index

    def rem_end(self):
        if self.tail is None:
            return None
        elif self.tail.prev is None:
            cp = self.tail.val
            self.tail = None
            self.head = None
            self.length -= 1
            return cp
        else:
            cp = self.tail.val
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length-=1
            return cp

    def add_disc(self, val):
        new_node = disk(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return

    def to_list(self):
        l = []
        trav = self.head
        while trav is not None:
            l.append(trav.val)
            trav = trav.next
        return l

    def __repr__(self):
        l = ""
        trav = self.head
        while trav is not None:
            l += str(trav.val)
            trav = trav.next
        return l

def move_peg(leaving, to):
    to.add_disc(leaving.rem_end())


def hanoi(num_disks, leaving, to, extra):
    count = 0
    if num_disks == 0:
        return count
    else:
        count += hanoi(num_disks - 1, leaving, extra, to)
        move_peg(leaving, to)
        count += 1
        print(draw_towers(leaving, to, extra))
        count += hanoi(num_disks - 1, extra, to, leaving)
        return count

def sort(towers):
    for i in range(len(towers) - 1) :
        for j in range(len(towers) - i):
            if towers[i].index > towers[i+j].index:
                copy = towers[i+j]
                towers[i+j] = towers[i]
                towers[i] = copy
    return towers

def draw_towers(a, b, c):
    s = ''
    list_index = sort([a,b,c])


    lv = list_index[0].to_list()
    lvl = list_index[0].length
    tl = list_index[1].to_list()
    tll = list_index[1].length
    el = list_index[2].to_list()
    ell = list_index[2].length

    for i in range(max(lvl, tll, ell)):
        if i < lvl:
            s += str(lv[lvl - i - 1]) + ' '
        else:
            s+= '  '
        if i < tll:
            s += str(tl[tll - i - 1]) + ' '
        else:
            s+= '  '
        if i < ell:
            s += str(el[ell - i - 1])
        s += '\n'
    return s

def hanoi_wrapper(disks):
    num_disks = disks
    leaving = peg(0)
    for i in range(num_disks):
        leaving.add_disc(i)
    to = peg(1)
    extra = peg(2)
    print(draw_towers(leaving, to, extra))
    print(hanoi(num_disks, leaving, to, extra))

def main():
    hanoi_wrapper(5)

if __name__ == "__main__":
    main()


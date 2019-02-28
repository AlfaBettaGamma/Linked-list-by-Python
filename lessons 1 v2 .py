#python 3.2.5
#python 3.5.2
import random
class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.leng = 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        return [] # здесь будет ваш код

    def delete(self, val, all=False):
        if(self.head == None):
            return
        old = node = self.head
        
        while node is not None:
            if (node.value == val):
                if (node.next == None):
                    self.tail = node
                past.next = node.next
                break
            past = node
            node = node.next
        pass # здесь будет ваш код

    def clean(self):
        self.__init__()
        pass # здесь будет ваш код

    def len(self):
        self.leng =0
        if(self.head == None):
            return
        node = self.head
        while node.next is not None:
            node = node.next
            self.leng +=1
        return self.leng+1 # здесь будет ваш код


    def insert(self, afterNode, newNode):
        pass # здесь будет ваш код
s_list = LinkedList()
y = random.randint(1,10)
for i in range(10):
    y = random.randint(1,10)
    s_list.add_in_tail(Node(y))
s_list.delete(5)
print("Длинна списка равна - ", s_list.len())
s_list.print_all_nodes()
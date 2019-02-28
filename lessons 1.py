#python 3.2.5
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
        list_val = []
        node = self.head
        while node is not None:
            if (node.value == val):
                list_val.append(val)
            node = node.next
        return list_val # здесь будет ваш код

    def delete(self, val, all=False):
        if(self.head == None):
            return
        node = self.head       
        while node.next is not None:
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
        if(self.head == None):
            self.tail = self.head = Node(newNode)
        node = self.head
        while node.next is not None:
            if(node.value == afterNode):
                node.next = Node(newNode)
                if(node.next.next == None):
                    self.tail = node.next
                break
            node = node.next
        pass # здесь будет ваш код

n1 = Node(12)
n2 = Node(55)
n1.next = n2 # 12 -> 55
s_list = LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list.add_in_tail(Node(128))
s_list.add_in_tail(Node(0))
s_list.add_in_tail(Node(12))
s_list.add_in_tail(Node(45))
s_list.delete(0)
print("Длинна списка равна - ",s_list.len())
print (s_list.find_all(12))
s_list.insert(12,31)
s_list.print_all_nodes()
import unittest
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
        past = node = self.head   
        if(all == False):
            while node.next is not None:
                if (node.value == val):
                    if (node.next == None):
                        self.tail = node
                    past.next = node.next
                    break
                past = node
                node = node.next
        else:
            while node is not None:
                if(node.next != None):
                    if(past.value == node.next.value):
                        node.next = node.next.next
                else:
                    past = node = past.next
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
        if(afterNode == None and node == None):
            self.head = node
            self.tail = self.head
        while node.next is not None:
            if(node.value == afterNode):
                node.next = Node(newNode)
                if(node.next.next == None):
                    self.tail = node.next
                break
            node = node.next
        pass # здесь будет ваш код

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        s_list = LinkedList()
        for i in range(10):
            self.A = s_list.add_in_tail(Node(random.randint(1,10)))
        self.B = s_list.add_in_tail(Node(123))

        for i in range(12):
            self.C = s_list.add_in_tail(Node("Hello"))


    def test_find_all(self):
        A.find_all()
        B.find_all()
        C.find_all()
      
    def test_delete(self):
        A.delete(random.randint(1,10), False)
        B.delete(random.randint(1,10), False)
        C.delete(random.randint(1,10), False)

if __name__ == '__main__':
    unittest.main()
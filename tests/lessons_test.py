
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
        if(self.head == None):
            return
        node = self.head
        while node is not None:
            if (node.value == val):
                list_val.append(node)
            node = node.next
        return list_val # здесь будет ваш код

    def delete(self, val, all=False):
        leng = 0
        if(self.head is None):
            return print("список пуст")
        node = self.head   
        if(all is False):  
            while node != None:
                if(leng == 0 and node.value == val):
                    self.head = node.next
                    leng += 1
                    break
                if(node.next != None):
                    if(node.next.value == val):
                        node.next = node.next.next
                        if(node.next is None):
                            self.tail = None
                        break
                    node = node.next
                else:
                    self.head = None
                    self.tail = None
        elif(all is True):
            while node != None:
                if(node.next != None):
                    if(node.next.value == val):
                        node.next = node.next.next
                        if(node.next is None):
                            self.tail = None
                    elif(leng == 0 and node.value == val):
                        self.head = node.next
                        leng += 1
                    else:
                        node = node.next
                else:
                    if(node.value == val):
                        self.head = None
                        self.tail = None
                    break
            pass # здесь будет ваш код
            
    def clean(self):
        self.__init__()
        pass # здесь будет ваш код

    def len(self):
        self.leng = 0
        if(self.head == None):
            return self.leng
        node = self.head
        while node is not None:
            node = node.next
            self.leng +=1
        return self.leng # здесь будет ваш код 

    def insert(self, afterNode, newNode):
        if(afterNode == None or self.head == None):
            self.head = Node(newNode)
            return
        node = self.head
        newN = Node(newNode)
        while node is not None:
            if(node.value == afterNode):
                newN.next = node.next
                node.next = newN
            node = node.next
        pass # здесь будет ваш код

class my_test:

    def test1_find_all(self):
        test = LinkedList()
        for i in range(100):
            y = random.randint(0,10)
            test.add_in_tail(Node(y))

        for j in range(10):
            y = random.randint(0,10)
            print(test.find_all(y))
            
    def test2_find_all(self): 
        test = LinkedList()
        for j in range(10):
            y = random.randint(0,10)
            test.add_in_tail(Node(y))
        test.clean()
        n = 1
        for j in range(10):
            y = random.randint(0,10)
            print(n,' - ' ,test.find_all(y))
            n += 1
 
    def test_del_false(self):
        test = LinkedList()
        test.add_in_tail(Node(9))
        test.len()
        if(test.len() == 1):
            print('В спсике один элемент!')
            test.print_all_nodes()
        test.delete(9)
        print('после удаления', test.head, test.tail, test.len())
        if(test.head is None and test.tail is None and test.len() == 0):
            print('список пуст!')              

    def test_del_true(self):
        test = LinkedList()
        test.add_in_tail(Node(0))
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(2))
        test.print_all_nodes()
        test.delete(2, True)
        if(test.head is None and test.tail is None and test.len() == 0):
            print("Список пустой!")
        else:
            print('Список после удаления')
            test.print_all_nodes()
            

    def test_clean(self):
        test1 = LinkedList()
        for j in range(10):
            y = random.randint(0,10)
            test1.add_in_tail(Node(y))
        test1.clean()
        if(test1.head is None and test1.len() == 0 and test1.tail is None):
            print("Список пустой")


    def test_len(self):
        test1 = LinkedList()
        for j in range(10):
            y = random.randint(0,10)
            test1.add_in_tail(Node(y))
        print(test1.len())
        test1.clean()
        if(test1.head is None and test1.len() == 0 and test1.tail is None):
            print("Список пустой")
        print(test1.len())

    def test_insert(self):
        test1 = LinkedList()
        v = "Вставка"
        for i in range(10):
            y = random.randint(0,10)
            test1.add_in_tail(Node(y))
        for i in range(20):
            y = random.randint(0,10)
            test1.insert(y, v)
            test1.print_all_nodes()
        
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
        if(self.head == None):
            return
        past = node = self.head   
        if(all == False):  
            while node is not None:
                if (node.value == val):
                    if(leng == 0):
                        self.head = self.head.next
                        return
                    if (node.next == None):
                        self.tail = node
                    past.next = node.next
                    break
                past = node
                node = node.next
                leng += 1
        else:
            while node is not None:
                if(leng == 0 and node.value == val):
                    self.head = node.next
                    leng += 1
                if(node.next != None):
                    if(node.next.value == val):
                        node.next = node.next.next
                        if(node.next == None):
                            self.tail = node
                    else:
                        node = node.next
                else:
                    node = node.next
            pass # здесь будет ваш код
            
    def clean(self):
        self.__init__()
        pass # здесь будет ваш код

    def len(self):
        self.leng = 0
        if(self.head == None):
            return
        node = self.head
        while node.next is not None:
            node = node.next
            self.leng +=1
        return self.leng+1 # здесь будет ваш код 

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

    def test1_find_all(self):
        test1 = LinkedList()
        for i in range(100):
            y = random.randint(0,10)
            test1.add_in_tail(Node(y))

        for j in range(10):
            y = random.randint(0,10)
            print(test1.find_all(y))
            
    def test2_find_all(self): 
        test1 = LinkedList()
        for j in range(10):
            y = random.randint(0,10)
            print(test1.find_all(y))

    def test_del_false(self):
        test1 = LinkedList()
        for i in range(10):
            y = random.randint(0,10)
            test1.add_in_tail(Node(y))
        for i in range(10):
            y = random.randint(0,10)
            len_1 = test1.len()
            test1.delete(y, False)
            len_2 = test1.len()
            test1.print_all_nodes()
            if(len_1 == len_2):
                print("Удаления не было(((")
            else:
                print("Удаление прошло успешно)")

    def test_del_true(self):
        test1 = LinkedList()
        for i in range(10):
            y = random.randint(0,10)
            test1.add_in_tail(Node(y))
        for i in range(10):
            y = random.randint(0,10)
            len_1 = test1.len()
            test1.delete(y, True)
            len_2 = test1.len()
            if(len_1 == len_2):
                print("Удаления не было(((")
            else:
                print("Удаление прошло успешно)")
            test1.print_all_nodes()

    def test_clean():
        test1 = LinkedList()
        for j in range(10):
            y = random.randint(0,10)
            test1.add_in_tail(Node(y))
        test1.clean()
        if(test1 != None):
            print('clean not work')

    def test_len():
        test1 = LinkedList()
        for j in range(10):
            y = random.randint(0,10)
            test1.add_in_tail(Node(y))
        print(test1.len())
        test1.clean()
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
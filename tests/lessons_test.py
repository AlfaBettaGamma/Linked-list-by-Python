
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
            return list_val
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
                    if(node.next is None):
                        self.head = None
                        self.tail = None
                    self.head = node.next
                    leng += 1
                    break
                if(node.next != None):
                    if(node.next.value == val):
                        node.next = node.next.next
                        if(node.next is None):
                            node = None
                            if(self.head is None and leng == 0):
                                self.tail = None
                            self.tail = self.head.next
                        break
                    node = node.next
                else:
                    self.head = None
                    self.tail = None
        elif(all is True):
            while node != None:
                if(node.next != None):
                    if(leng == 0 and node.value is val):
                        node = node.next
                    elif(node.next.value is val):
                        node.next = node.next.next
                        if(node.next is None):
                            node = None
                            self.tail = self.head.next
                    else:
                        node = node.next
                        leng += 1
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
        for j in range(1):
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
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(0))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(2))
        test.delete(2, True)
        test.print_all_nodes()
        if(test.head is None and test.tail is None and test.len() == 0):
            print("Список пустой!")
        else:
            print('Список после удаления')
            test.print_all_nodes()
        
    def test_del_true1(self):
        test = LinkedList()
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(6))
        test.add_in_tail(Node(2))
        len_1 = test.len()
        test.delete(2, True)
        len_2 = test.len()
        len_del = len_1 - len_2
        if(len_del == len_1 and test.head is None and test.len() == 0 and test.tail is None):
            print('Список пустой. Удаленно было ',len_del ,'элементов.')
        else:
            print('В списке осталось - ', len_2,'элементов.' , 'Удаленно было - ', len_del, 'элементов.')

    def test_del_true2(self):
        test = LinkedList()
        test.add_in_tail(Node(0))
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(2))       
        y = 2
        test.print_all_nodes()
        len_1 = test.len()
        for i in range(test.len()):
            if(y == test.head.value and test.head.next is None):
                print('Удалятся будет последний узел')
        test.delete(y, True)
        len_2 = test.len()
        len_del = len_1 - len_2
        for i in range(test.len()):
            if (y != test.head.value):
                print('Удаление последнего узла прошло успешно!')
                break
        test.print_all_nodes()
        
        print('Удаленно (',len_del,' элементов). Узла с значением -', y)

    def test_del_true3(self):
        test = LinkedList()
        test.add_in_tail(Node(1))
        test.add_in_tail(Node(2))
        test.add_in_tail(Node(3))
        test.add_in_tail(Node(3))
        test.add_in_tail(Node(3))
        test.add_in_tail(Node(3))
        len_1 = test.len()
        test.delete(3, True)
        len_2 = test.len()
        if (len_1 != len_2):
            print('Общее количество элементов до удаления - ', len_1, 'оставшееся количество элементов - ', len_2)
        if(test.len() == 2):
            print(test.head.value, test.tail.value)        

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
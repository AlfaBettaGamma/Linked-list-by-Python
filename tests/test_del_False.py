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

    def delete(self, val, all=False):
        leng = 0
        if(self.head == None):
            return
        past = node = self.head   
        if(all == False):  
            while node is not None:
                if(leng == 0 and node.value == val):
                    self.head = node.next
                    leng += 1
                    break
                if(node.next != None):
                    if(node.next.value == val):
                        node.next = node.next.next
                        if(node.next == None):
                            self.head = None
                        break
                    node = node.next
        else:
            while node is not None:
                if(node.next != None):
                    if(node.next.value == val):
                        node.next = node.next.next
                        if(node.next is None):
                            self.head = None
                    if(leng == 0 and node.value == val):
                        self.head = node.next
                        leng += 1
                    node = node.next
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
            if(test1.len() == 1):
                print("В списке один элемент")
            test1.print_all_nodes()
            if(len_1 == len_2):
                print("Удаления не было(((")
            else:
                print("Удаление прошло успешно)")
            if(test1.head is None and test1.len() == 0 and self.tail is None):
                print("Список пустой")
                break

    def test1_del_false(self):
        node = self.head
        test1 = LinkedList()
        test1.add_in_tail(Node(9))
        test1.len()
        if(test1.len() == 1):
            print('В списке один элемент!')
        test1.delete(9)
        if(test1.head is None and test1.len() == 0 and self.tail is None):
            print("Список пустой")
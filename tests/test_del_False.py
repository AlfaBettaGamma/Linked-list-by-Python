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
                if(leng == 0 and node.value == val):
                    self.head = node.next
                    leng += 1
                    break
                if(node.next != None):
                    if(node.next.value == val):
                        node.next = node.next.next
                        if(node.next == None):
                            self.tail = node
                        break
                    else:
                        node = node.next
                else:
                    node = node.next
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

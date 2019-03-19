class Node:
 def __init__(self, v, next = None):
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
    leng = 0
    if(self.head == None):
     return
    node = self.head
    while node is not None:
     if (node.value == val):
        list_val.append(leng)
     leng += 1
     node = node.next
    return list_val # здесь будет ваш код

 def delete(self, val, all = False):
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
        if (node.next != None):
         if past.value == node.next.value and past.value == val:
            node.next = node.next.next
        else:
         past=node = past.next
        node=node.next
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
        self.head = Node(newNode, None)
    node = self.head
    while node is not None:
        if(node.value == afterNode):
            node.next = Node(newNode, node.next)
            if(node.next.next == None):
                self.tail = node.next
            break
        node = node.next
    pass # здесь будет ваш код
# doubly linked list. used in browser history, undo/redo functionality

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last
            
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            raise ValueError("Previous node is not in the list")
        new_node = Node(data)
        new_node.next = prev_node.next
        
        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next = new_node
        new_node.prev = prev_node
        
    def delete_node(self, key):
        temp = self.head
        
        while temp:
            if temp.data == key:
                break
            temp = temp.next
            
        if temp is None:
            print("Key not found in the list")
            return
        
        if temp.prev is None:
            self.head = temp.next
            if self.head:
                self.head.prev = None
        else:
            temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev
        
        temp = None
        
    def print_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("None")
        
    def print_backward(self):
        temp = self.head
        if temp is None:
            return
        
        while temp.next:
            temp = temp.next
            
        while temp:
            print(temp.data, end="<->")
            temp = temp.prev
        print("None")
        
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_beginning(5)
    dll.insert_after_node(dll.head.next, 15)
    dll.insert_at_end(25)
    
    dll.print_forward()
    dll.print_backward()
    
    dll.delete_node(20)
    dll.print_forward()
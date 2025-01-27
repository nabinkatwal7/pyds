# singly linked list. usages: todo app, undo functionality, etc
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def delete_beginning_node(self):
        if self.head is None:
            return
        self.head = self.head.next
        
    def delete_end_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        
    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        if temp is None:
            return
        
        prev.next = temp.next        
        temp = None
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
        
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    
    linked_list.insert_at_beginning(1)
    linked_list.insert_at_beginning(2)
    linked_list.insert_at_beginning(3)
    linked_list.insert_at_end(4)
    linked_list.insert_after_node(linked_list.head.next, 5)
    linked_list.print_list()
    
    
    linked_list.delete_beginning_node()
    
    linked_list.delete_end_node()
    
    linked_list.print_list()
        
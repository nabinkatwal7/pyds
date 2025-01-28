class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.size = 0      

    def is_empty(self):
        return self.size == 0

    def add_front(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def add_rear(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty. Cannot remove from front.")
        value = self.front.value
        if self.front == self.rear: 
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return value

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty. Cannot remove from rear.")
        value = self.rear.value
        if self.front == self.rear:  
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty. Cannot peek at front.")
        return self.front.value

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty. Cannot peek at rear.")
        return self.rear.value

    def __len__(self):
        return self.size

    def __str__(self):
        elements = []
        current = self.front
        while current:
            elements.append(str(current.value))
            current = current.next
        return " <-> ".join(elements)


if __name__ == "__main__":
    dq = Deque()

    dq.add_front(10)
    dq.add_front(20)
    dq.add_rear(30)
    dq.add_rear(40)

    print("Deque:", dq) 

    print("Removed from front:", dq.remove_front()) 
    print("Removed from rear:", dq.remove_rear())   

    print("Deque after removal:", dq) 

    print("Front element:", dq.peek_front())  
    print("Rear element:", dq.peek_rear())    

    print("Size of deque:", len(dq))  
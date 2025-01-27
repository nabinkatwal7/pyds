class Node:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_task(self, description, priority):
        new_node = Node(description, priority)
        if not self.head:
            self.head = self.tail = new_node
        else:
            current = self.head
            while current and current.priority >= priority:
                current = current.next
            if not current:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                new_node.next = current
                new_node.prev = current.prev
                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node
                current.prev = new_node
    
    def remove_task(self, description):
        current = self.head
        while current:
            if current.description == description:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False
    
    def move_task_up(self, description):
        current = self.head
        while current:
            if current.description == description and current.prev:
                prev_node = current.prev
                prev_node.description, current.description = current.description, prev_node.description
                prev_node.priority, current.priority = current.priority, prev_node.priority
                return True
            current = current.next
        return False
    
    def move_task_down(self, description):
        current = self.head
        while current:
            if current.description == description and current.next:
                next_node = current.next
                next_node.description, current.description = current.description, next_node.description
                next_node.priority, current.priority = current.priority, next_node.priority
                return True
            current = current.next
        return False
    
    def display_tasks(self):
        current = self.head
        while current:
            print(f"Task: {current.description} | Priority: {current.priority}")
            current = current.next
            
class TaskScheduler:
    def __init__(self):
        self.tasks = DoublyLinkedList()
    
    def add_task(self):
        description = input("Enter task description: ")
        priority = input("Enter task priority: (High/Medium/low)").capitalize()
        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority. Task not added.")
            return
        self.tasks.add_task(description, priority)
        print("Task added successfully.")
        
    def remove_task(self):
        description = input("Enter task description: ")
        if self.tasks.remove_task(description):
            print("Task removed successfully.")
        else:
            print("Task not found!")
            
    def move_task_up(self):
        description = input("Enter task description to move up: ")
        if self.tasks.move_task_up(description):
            print("Task moved up successfully.")
        else:
            print("Task not found or already at the top!")
            
    def move_task_down(self):
        description = input("Enter task description to move down: ")
        if self.tasks.move_task_down(description):
            print("Task moved down successfully.")
        else:
            print("Task not found or already at the bottom!")
            
    def display_tasks(self):
        print("\ncurrent tasks:")
        self.tasks.display_tasks()
        
    def run(self):
        while True:
            print("\nMenu:")
            print("1. Add task")
            print("2. Remove task")
            print("3. Move task up")
            print("4. Move task down")
            print("5. Display tasks")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.remove_task()
            elif choice == "3":
                self.move_task_up()
            elif choice == "4":
                self.move_task_down()
            elif choice == "5":
                self.display_tasks()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.run()
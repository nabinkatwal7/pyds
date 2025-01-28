class Stack:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)
    
class Browser:
    def __init__(self):
        self.history = Stack()
        
    def visit_page(self, page):
        print(f"Visiting page: {page}")
        self.history.push(page)
        
    def go_back(self):
        previous_page = self.history.pop()
        if previous_page:
            print(f"Going back to: {previous_page}")
        else:
            print("No previous page available.")
            
    def current_page(self):
        current = self.history.peek()
        if current:
            print(f"Current page: {current}")
        else:
            print("No current page available.")
            
    def show_history(self):
        print(f"History: {self.history}")
        
if __name__ == "__main__":
    browser = Browser()
    
    browser.visit_page("https://www.example.com")
    browser.visit_page("https://www.google.com")
    browser.visit_page("https://www.python.org")
    
    browser.show_history()
    
    browser.go_back()
    browser.current_page()
    
    browser.show_history()
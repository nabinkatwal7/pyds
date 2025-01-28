class Queue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)
    
class PrintQueue:
    def __init__(self):
        self.queue = Queue()
        
    def add_print_job(self, document):
        print(f"Adding print job for document: {document}")
        self.queue.enqueue(document)
        
    def process_print_job(self):
        job = self.queue.dequeue()
        if job:
            print(f"Processing print job for document: {job}")
        else:
            print("No print jobs available.")
            
    def show_queue(self):
        print(f"Print queue: {self.queue}")
        
if __name__ == "__main__":
    printer = PrintQueue()
    
    printer.add_print_job("Document1.pdf")
    printer.add_print_job("Document2.pdf")
    printer.add_print_job("Document3.pdf")
    
    printer.show_queue()
    
    printer.process_print_job()
    printer.process_print_job()
    printer.process_print_job()
    
    printer.process_print_job()

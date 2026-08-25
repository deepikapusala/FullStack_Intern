import time
class Timer: #class acts as CoMa
    def __enter__(self): #enter runs when we enter 'with' block
        self.start = time.time()
        return self #return Timer object

    def __exit__(self, exc_type, exc_value, traceback):#this runs when 'with' block finishes
        end = time.time()
        print("\nException type:", exc_type)
        print("Exception value:", exc_value)
        print("Traceback:", traceback)
        print("Total ka value: ",total)
        print("Time taken:", end - self.start, "seconds")
        
with Timer():
    total = 0

    for i in range(100):
        total += i
        

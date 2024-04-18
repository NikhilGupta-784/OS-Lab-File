from threading import Thread
from time import sleep

class DekkerMutex:
    def __init__(self):
        self.flag = [False, False]  # Flags for each process
        self.turn = 0               # The turn variable to indicate whose turn it is
        self.other = lambda i: 1 - i  # Helper function to get the index of the other process

    def lock(self, process_id):
        self.flag[process_id] = True
        while self.flag[self.other(process_id)] and self.turn == self.other(process_id):
            # Wait while other process is in critical section and it's their turn
            pass

    def unlock(self, process_id):
        self.turn = self.other(process_id)
        self.flag[process_id] = False

# Example usage
def process1(mutex):
    for _ in range(5):
        mutex.lock(0)
        print("Process 1 is in critical section")
        sleep(1)
        mutex.unlock(0)

def process2(mutex):
    for _ in range(5):
        mutex.lock(1)
        print("Process 2 is in critical section")
        sleep(1)
        mutex.unlock(1)

if __name__ == "__main__":
    mutex = DekkerMutex()
    thread1 = Thread(target=process1, args=(mutex,))
    thread2 = Thread(target=process2, args=(mutex,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

from threading import Thread, Lock
import time
import random

class ReadersWriters:
    def __init__(self):
        self.data = 0
        self.readers_count = 0
        self.mutex = Lock()
        self.resource = Lock()

    def reader(self, reader_id):
        while True:
            self.mutex.acquire()
            self.readers_count += 1
            if self.readers_count == 1:
                self.resource.acquire()
            self.mutex.release()

            # Reading data
            print(f"Reader {reader_id} is reading data: {self.data}")

            self.mutex.acquire()
            self.readers_count -= 1
            if self.readers_count == 0:
                self.resource.release()
            self.mutex.release()

            time.sleep(random.random())  # Simulating some reading time

    def writer(self, writer_id):
        while True:
            self.resource.acquire()

            # Writing data
            self.data += 1
            print(f"Writer {writer_id} is writing data: {self.data}")

            self.resource.release()

            time.sleep(random.random())  # Simulating some writing time

if __name__ == "__main__":
    rw = ReadersWriters()

    # Creating reader threads
    for i in range(3):
        reader_thread = Thread(target=rw.reader, args=(i,))
        reader_thread.start()

    # Creating writer threads
    for i in range(2):
        writer_thread = Thread(target=rw.writer, args=(i,))
        writer_thread.start()

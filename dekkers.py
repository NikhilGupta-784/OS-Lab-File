import threading
import time

NUM_THREADS = 2

wants_to_enter = [False] * NUM_THREADS
turn = 0

semaphore = threading.Semaphore()

def dekker(thread_id):
    global turn
    for i in range(5):
        wants_to_enter[thread_id] = True
        while wants_to_enter[1 - thread_id]:
            if turn != thread_id:
                wants_to_enter[thread_id] = False
                while turn != thread_id:
                    pass
                wants_to_enter[thread_id] = True

        print(f"Thread {thread_id} is in critical section")
        time.sleep(0.5)
        turn = 1 - thread_id
        wants_to_enter[thread_id] = False

def main():
    threads = []
    for i in range(NUM_THREADS):
        t = threading.Thread(target=dekker, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()

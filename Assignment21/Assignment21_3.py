import threading


counter = 0
lock = threading.Lock()


def increment_counter(times):

    global counter

    for _ in range(times):

        lock.acquire()

        counter += 1

        lock.release()


def main():

    thread1 = threading.Thread(target=increment_counter, args=(100000,))
    thread2 = threading.Thread(target=increment_counter, args=(100000,))
    thread3 = threading.Thread(target=increment_counter, args=(100000,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print("Final Counter Value :", counter)


if __name__ == "__main__":
    main()
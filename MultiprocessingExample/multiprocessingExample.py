# multiprocessing = running in parallel on different cpu cores, bypasses GIL used for threading
# multiprocessing = better for cpu bound tasks (heaby cpu usage)
# multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(cpu_count())
    
    a = Process(target=counter, args=(500000,))
    b = Process(target=counter, args=(500000,))

    a.start()
    b.start()

    a.join()
    b.join()

    print("Finished in:", time.perf_counter(), "seconds")

if __name__ == '__main__':
    main()
# daemon thread =  a thread that runds in the background, not important dor program to run
# your program will noi wait dor daemon threads to complete before exiting
# non-daemon threads cannot normally be killed, stay alive until task is complete

# ex: background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)
# print(x.isDaemon())

answer = input("Do you wish to exit?")
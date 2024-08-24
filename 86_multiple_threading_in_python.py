# Multithreading in Python
# Multithreading is a technique in programming that allows multiple threads of execution to run concurrently 
# within a single process. In Python, we can use the threading module to implement multithreading.
#  In this tutorial, we will take a closer look at the threading module and its various functions
#  and how they can be used in Python.

# Importing Threading
# We can use threading by importing the threading module.

# import threading
# Creating a thread
# To create a thread, we need to create a Thread object and then call its start() method. 
# The start() method runs the thread and then to stop the execution, we use the join() method. 
# Here's how we can create a simple thread.

import threading
def my_func():
  print("Hello from thread", threading.current_thread().name)
  thread = threading.Thread(target=my_func)
  thread.start()
  thread.join()
# Functions
# The following are some of the most commonly used functions in the threading module:

# threading.Thread(target, args): This function creates a new thread that runs the target function
#  with the specified arguments.

# threading.Lock(): This function creates a lock that can be used to synchronize access to shared resources 
# between threads.

# Creating multiple threads
# Creating multiple threads is a common approach to using multithreading in Python. 
# The idea is to create a pool of worker threads and then assign tasks to them as needed. T
# his allows you to take advantage of multiple CPU cores and process tasks in parallel.
import threading
import time
from concurrent.futures import ThreadPoolExecutor
# def func(seconds):
#     time.sleep(seconds)
#     print(f"This Function took {seconds} seconds to run")
#     return seconds
# func(4)
# func(2)
# func(1)
# def main():
#  time1=time.perf_counter()
#  t1=threading.Thread(target=func, args=[4])
#  t2=threading.Thread(target=func, args=[2])
#  t3=threading.Thread(target=func, args=[1])
#  t1.start()
#  t2.start()
#  t3.start()
#  t1.join()
#  t2.join()
#  t3.join()
#  time2=time.perf_counter()
#  time=time2-time1
#  print(f"The Function total {time} time")
# def poolingDemo():
#   with ThreadPoolExecutor() as executor1:
#     future1 = executor1.submit(func, 1)
#   with ThreadPoolExecutor() as executor2:
#     future2 = executor2.submit(func, 2)
#   with ThreadPoolExecutor() as executor3:
#     future3 = executor3.submit(func, 1)
#   print(future1.result())
#   print(future2.result())
#   print(future3.result())
# poolingDemo()
# l=[3,5,9,10]
# def poolingDemo():
#   with ThreadPoolExecutor() as executor:
#     results=executor.map(func, l)
#     for result in results:
#       print(result)
# poolingDemo()

# def func():
#     if __name__=="__main__":
#         print("Task processed")
# tasks=[10,13,15,18,20,12,1,5,8,9]
# thread=[]
# threads=threading.Thread(target=func, args=(tasks, ))
# thread.append(threads)
# threads.start()
# for task in tasks:
#     print("The task are: ", task)
# for threads in thread:
#     thread.join()

# Using a lock to synchronize access to shared resources
# When working with multithreading in python, locks can be used to synchronize access to shared resource
# s among multiple threads. A lock is an object that acts as a semaphore, allowing only one thread at a time 
# to execute a critical section of code.
#  The lock is released when the thread finishes executing the critical section.

# Conclusion
# As you can see, the threading module provides a simple and efficient way to implement multithreading in Python. Whether you need to create a new thread, run a function across multiple input values, or synchronize access to shared resources, the threading module has you covered.

# In conclusion, the threading module is a powerful tool for parallelizing code in Python.
#  Whether you are a beginner or an experienced Python developer, the threading module is an essential tool
#  to have in your toolbox. With multithreading,
#  you can take advantage of multiple CPU cores and significantly improve the performance of your code.

def increment(counter, lock):
    for i in range(10000):
      lock.acquire()
      counter+=1
      lock.release()
if __name__ == "__main__":
    counter=0
    lock=threading.Lock()
    threads=[]
    for i in range(20):
      thread=threading.Thread(target=increment, args=(counter, lock))
      threads.append(thread)
      thread.start()
    for thread in threads:
        thread.join()
    print(thread)
print("Counter Value: ", counter)


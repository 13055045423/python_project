from multiprocessing import Process,Queue
import os

data_queue = Queue(maxsize=10)

def write_data(num,data_queue):
    print(num)
    for i in range(0,num):
        data_queue.put(i)
    print(os.getpid(),data_queue.full())

def read_data(data_queue):
    print('正在读取',os.getpid())
    print(data_queue.qsize())
    for i in range(0,data_queue.qsize()):
        print(data_queue.get())

if __name__ == '__main__':
    print('主进程开启',os.getpid())
    process1=Process(target=write_data,args=(10,data_queue))
    process1.start()
    process1.join()
    process2=Process(target=read_data,args=(data_queue,))
    process2.start()
    process2.join()
    print('主进程结束',os.getpid())


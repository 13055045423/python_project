from threading import Thread
import threading
import time
#检测线程之间的资源共享
data= []
def download_image(url,num):
    """下载图片"""
    global data
    time.sleep(2)
    print(url,num)
    data.append(num)

def read_data():
    global data
    for i in data:
        print(i)

if __name__ == '__main__':
    #获取当前线程的名称theading.currentThead().name
    print('主线程开启',threading.currentThread().name)
    #创建一个子线程
    """
    target=None.线程要执行的目标函数
    name=None创建线程时，指定线程名称
    args=()为目标函数,传递参数(tuple元祖类型)
    """
    thread_sub1=Thread(
        target=download_image,
        name='下载线程',
        args=('https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=338874098,844915032&fm=200&gp=0.jpg',1)
    )
    thread_sub2 = Thread(
        target=read_data,
        name='读取线程',
    )

    #是否开启守护进程（在开启线程之前设置）
    #daemon:False在主线程结束的时候，会检测子线程任务是否结束
    #如果子线程中任务没有结束，则会让子线程任务正常结束
    # daemon:True 在主线程结束的时候,会检测子线程任务是否结束,
    # 如果子线程中任务没有结束,则会让子线程跟随主线程一起结束
    #启动线程
    thread_sub1.start()
    #join()阻塞等待子线程中的任务执行完毕后,子回到主线程中继续执行
    thread_sub1.join()

    #开启线程
    thread_sub2.start()

    thread_sub2.join()

    print('主线程结束',threading.currentThread().name)
    
1.实现多任务的方式
多线程
多进程
协程
多线程+多进程

为什么你能够实现多任务？

并行：同时发起,同时执行(4核,4个任务)
并发：同时发起,单个执行

在python语言中,并不能够正真意义上实现多线程,因为CPython解释器
有一个全局的GIL解释器锁,来保证同一时刻只有一个线程在执行

线程:是cpu执行的一个基本单元,暂用的资源非常少,并且线程和线程之间的资源
是共享的,线程是依赖于进程而存在的,多线程一般适用于I/O密集型操作,线程的
执行是无序的
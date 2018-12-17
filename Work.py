import queue,time,sys
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
	
server_addr='127.0.0.1'
print('Connect to address:%s'%server_addr)
M=QueueManager(address=(server_addr,5000),authkey=b'abc')
try:
    M.connect()
except:
    print("Please connect Master Server...")
	
task=M.get_task_queue()
result=M.get_result_queue()
	
for i in range(10):
    try:
        n=task.get(timeout=1)
        print("run task %s * %s ..."%(n,n))
        r='%d*%d=%d'%(n,n,n**2)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('Please input task.')
			
print('worker exit')
print('next')
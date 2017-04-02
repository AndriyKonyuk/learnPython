import time, random, threading

lock = threading.Lock()

def worker(file: object, *args):
    '''
    worker function writes two strings with random pause to
    shared file using synchronization primitive
    :param file: file-object
    :return:
    '''
    with lock:
        file.write(threading.current_thread().getName() + ': ' + 'started.\n')
        time.sleep(random.random()*2)
        file.write(threading.current_thread().getName() + ': ' + 'done.\n')


if __name__ == '__main__':

    file = open('test.txt', 'a')
    for i in range(10):
        t = threading.Thread(target=worker, args=(file, ))
        t.start()
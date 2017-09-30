#coding = utf-8

import threading
import Queue
import sys
import os
from subprocess import Popen,PIPE

class Engine(threading.Thread) :

    def __init__(self,queue) :
        
        threading.Thread.__init__(self)
        self._queue = queue


    def run(self) :

        while not self._queue.empty() :
            ip = self._queue.get()
            ping = Popen(['cmd.exe','ping '+ip],stdin=PIPE,stdout=PIPE)
            data = ping.stdout.read()

            if 'ttl' in data :
                sys.stdout.write(ip+'\n')


def main() :

    threadpool = []
    count = 10
    queue = Queue.Queue()

    for i in range(1,255) :
        queue.put('153.37.232.' + str(i))

    for i in range(count) :
        threadpool.append(Engine(queue))

    for i in threadpool :
        i.start()

    for i in threadpool :
        i.join

if __name__ == '__main__' :
    main()
    

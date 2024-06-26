from Recognition import listen
from Commands import action

import threading

global queue
class Queue(object):
    def __init__(self):
        self.item= []

    def __repr__(self):
        return "{}".format(self.item)

    def __str__(self):
        return "{}".format(self.item)

    def enque(self, add):
        self.item.insert(0, add)
        return True

    def size(self):
        return len(self.item)

    def isempty(self):
        if self.size() == 0:
             return True
        else:
             return False 
    
    def deque(self):
        if self.size() == 0:
            return None
        else:
            return self.item.pop()
        
queue = Queue()    

listenT = threading.Thread(target=listen())
commandT = threading.Thread(target=action, args=(queue.deque(),))

listenT.start()
listenT.join()
commandT.start()
# Arg = listen()
# action(Arg)
from Recognition import listen
from Commands import action

import threading
from threading import Thread
import Vars


listenT = threading.Thread(target=listen())
commandT = threading.Thread(target=action, args=(Vars.queue.deque(),))
listenT.start()
listenT.join()

commandT.start()
while Vars.x:
    # Thread.start_new_thread( listen)
    # Thread.join()
    # Thread.start_new_thread( commandT)
    pass
    

# Arg = listen()
# action(Arg)
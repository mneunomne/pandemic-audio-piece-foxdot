# test threading 

import time, threading

WAIT_SECONDS = 1
echo=0.1
def foo():
    print(time.ctime())
    threading.Timer(WAIT_SECONDS, foo).start()
    echo+=0.1
    play('x',dur=2, echo=echo)
    
foo()


from twisted.internet import task
from twisted.internet import reactor

def tick():
    pass

def main():
    tick_interval = 0.25
    tick_cycle = task.LoopingCall(tick)
    tick_cycle.start(tick_interval) # call every second

    reactor.run()

if __name__ == "__main__":
    main()

import threading

threads = 4
nth_fibonacci_term = 38


class WorkerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print "Initialising", self.getName()

    def run(self):
        print self.getName(), "started!"
        self.f(nth_fibonacci_term)
        print self.getName(), "finished!"

    def f(self, n):
        if n < 2:
            return n
        else:
            return self.f(n - 1) + self.f(n - 2)


if __name__ == '__main__':
    for i in range(threads):
        WorkerThread().start()

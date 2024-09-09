from threading import *
import time
import sys

def main():
    d1 = Display1_5()
    d2 = Display6_10()
    d1.start()
    d2.start()


class Display1_5(Thread):

    def run(self):
        for i in range(1, 6):
            sys.stdout.write('display1_5 ' + str(i) + "\n")
            time.sleep(1)

class Display6_10(Thread):

    def run(self):
        for i in range(6, 11):
            sys.stdout.write('display6_10 ' + str(i) + "\n")
            time.sleep(1)

main()

import time
import sys

if __name__=='__main__':
    try:
        t = time.time()
        print(f"Timetamp:{t}")

        while True:
            key = input('\npress any key to exit:')
            break
    except KeyboardInterrupt:
        sys.exit(0)
import time

print('Press Enter to begin, Press Ctrl + C to stop')
input()

print('start')
startTime = time.time()

while True:
    try:
        print(round(time.time() - startTime, 2), 'secs')
    except KeyboardInterrupt as e:
        print('end')
        endTime = time.time()
        print('total time:', endTime - startTime)
        break


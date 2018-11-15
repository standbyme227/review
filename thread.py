import threading, time

# def myThread(id):
#     for i in range(10):
#         print("id {} --> count {}".format(id, i))
#         time.sleep(0)
#
# if __name__ =="__main__":
#
#     threads = []
#
#     for i in range(2):
#         th = threading.Thread(target=myThread, args=(i,))
#         th.start()
#         threads.append(th)
#
#     for th in threads:
#         th.join()
#     print("끝")


def myThread(id):
    for i in range(10):
        print("id {} --> count {}".format(id, i))
        time.sleep(0)  # Thread 종료

threads = []  # 쓰레드 객체를 저장하는 리스트 (쓰레드 관리 리스트)

for i in range(2):
    th = threading.Thread(target=myThread, args=(i,))
    th.start()  # 쓰레드 시작
    threads.append(th)  # thread 객체를 리스트에 저장

for th in threads:
    th.join()  # 각 쓰레드가 종료될때까지 대기
print("끝")


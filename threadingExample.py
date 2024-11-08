import threading

def print_message(message):
    
    print(message)

thread1 = threading.Thread(target=print_message, args=("Elzio",))
thread2 = threading.Thread(target=print_message, args=("Lihat Mama",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print ("selesai")
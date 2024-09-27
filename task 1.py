import queue
import time
import random

queue = queue.Queue()

id_counter = 0

def generate_request():
    global id_counter
    id_counter += 1
    r = {
        'id': id_counter,
        'msg': f'I am request #{id_counter}'
    }
    queue.put(r)
    print(f'#{r["id"]} claim added to the queue')

def process_request():
    if not queue.empty():
        r = queue.get()
        print(f'Handling claim #{r["id"]}: {r["msg"]}')
        time.sleep(0.5)
        print(f'Claim #{r["id"]} successfully handled')
    else:
        print('Queue is empty')

def main():
    try:
        while True:
            if random.random() < 0.7: 
                generate_request()
            process_request()

            time.sleep(0.75)
    except KeyboardInterrupt:
        print("\nExit")

if __name__ == "__main__":
    main()

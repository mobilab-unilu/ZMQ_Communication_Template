import random
import zmq
import time

import Settings
from Logger import get_logger


logger = get_logger()

def dealer_1():
    context = zmq.Context()
    dealer_socket = context.socket(zmq.DEALER)
    dealer_socket.setsockopt(zmq.IDENTITY, Settings.dealer1_ID)
    dealer_socket.connect(Settings.router_localhost)

    time.sleep(Settings.waiting_time)
    flag = True

    while True:
        # Simulate operations
        time.sleep(random.uniform(1, 3))

        if flag:
            # Send a message to dealer 2
            content = b'Message_from_dealer_1'
            dealer_socket.send_multipart([Settings.dealer2_ID, content])
            logger.info(f'DEALER1: Message sent to DEALER2')
            flag = False

        if dealer_socket.poll(timeout=100):
            multipart = dealer_socket.recv_multipart()
            sender_id, content = multipart
            logger.info(f'DEALER1: Received message from {sender_id.decode()} with message {content.decode()}')
            flag = True


if __name__ == '__main__':
    dealer_1()
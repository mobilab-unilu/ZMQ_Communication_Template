import random
import zmq
import time

import Settings
from Logger import get_logger


logger = get_logger()

def dealer_2():
    context = zmq.Context()
    dealer_socket = context.socket(zmq.DEALER)
    dealer_socket.setsockopt(zmq.IDENTITY, Settings.dealer2_ID)
    dealer_socket.connect(Settings.router_localhost)

    time.sleep(Settings.waiting_time)

    while True:
        # Simulate operations
        time.sleep(random.uniform(1, 3))

        if dealer_socket.poll(timeout=100):
            multipart = dealer_socket.recv_multipart()
            sender_id, content = multipart
            logger.info(f'DEALER2: Received message from {sender_id.decode()} with message {content.decode()}')

            time.sleep(random.uniform(1, 3))
            message = b'Message_from_dealer_2'
            dealer_socket.send_multipart([sender_id, message])
            logger.info(f'DEALER2: Message sent to DEALER1')

if __name__ == '__main__':
    dealer_2()
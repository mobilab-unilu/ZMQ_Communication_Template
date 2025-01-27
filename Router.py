import time
import zmq
import Settings
from Logger import get_logger


logger = get_logger()

def router():
    context = zmq.Context()

    # Setup router
    router_socket = context.socket(zmq.ROUTER)
    router_socket.bind(Settings.router_localhost)

    time.sleep(Settings.waiting_time)

    while True:
        # Receive multipart message
        multipart = router_socket.recv_multipart()
        if len(multipart) == 3:
            sender_id, dest_id, content = multipart
            logger.info(f'ROUTER: Received message from {sender_id.decode()} to {dest_id.decode()} with message {content.decode()}')
            router_socket.send_multipart([dest_id, sender_id, content])
        else:
            logger.warning(f'ROUTER: Received ill-formed message')

if __name__ == '__main__':
    router()
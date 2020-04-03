import socket

from message_wrapper import get_message
import settings

udp_server_socket = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_DGRAM
)

udp_server_socket.bind(settings.SERVER_ADDRESS)
print('UDP server up and listening')

first_message, address = udp_server_socket.recvfrom(settings.BUFFER_SIZE)
print(first_message)
first_response = str.encode('I say: "hello!"')
print(first_response)
udp_server_socket.sendto(first_response, address)

while(True):
    message, address = udp_server_socket.recvfrom(settings.BUFFER_SIZE)
    print(f'Client says: {message}')

    response = get_message(settings.PROMPT)
    udp_server_socket.sendto(response, address) 
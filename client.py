import socket

from message_wrapper import get_message
import settings

udp_client_socket = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_DGRAM
)

print('UDP client up and ready to send.')


first_message = str.encode('You say: "beep"')
print(first_message)
udp_client_socket.sendto(first_message, settings.SERVER_ADDRESS)
first_response, _ = udp_client_socket.recvfrom(settings.BUFFER_SIZE)
print(first_response)

while True:
    message = get_message(settings.PROMPT)
    udp_client_socket.sendto(message, settings.SERVER_ADDRESS)

    response_from_server, _ = udp_client_socket.recvfrom(settings.BUFFER_SIZE)
    print(f'Server says: {response_from_server}')
from decouple import config

SERVER_IP = config('SERVER_IP')
SERVER_PORT = config('SERVER_PORT', cast=int)
SERVER_ADDRESS = (SERVER_IP, SERVER_PORT)
BUFFER_SIZE=config('BUFFER_SIZE', cast=int)
PROMPT = config('PROMPT')

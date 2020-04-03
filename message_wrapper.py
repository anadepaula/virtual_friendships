def get_message(prompt):
    message = input(prompt)
    encoded_message = str.encode(message)
    return encoded_message

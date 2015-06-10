import sys

def normalize(byte, min_byte, max_byte):
    '''
    Normalizes byte so that it falls within byte range
    '''
    # inclusive range
    byte_range = max_byte - min_byte + 1
    normal_byte = (byte - min_byte) % byte_range
    return normal_byte + min_byte

def cipher(message, shift):
    '''
    Returns a ciphered message based on the shift.
    '''
    message = message.upper()
    begin_byte = ord("A")
    end_byte = ord("Z")
    encrypted_message = ""

    for ch in message:
        byte_position = ord(ch)
        # don't manipulate non-alphabetic characters
        if byte_position > end_byte or byte_position < begin_byte:
            encrypted_message += ch
        else:
            new_byte = normalize(byte_position + shift, begin_byte, end_byte)
            encrypted_message += chr(new_byte)

    return encrypted_message


def usage():
    return "Usage: {} [encrypt|decrypt] <message>".format(sys.argv[0])
    
def main():
    if len(sys.argv) != 3:
        print "Wrong number of arguments."
        print usage()

    command = sys.argv[1]
    message = sys.argv[2]

    shift = 3
    if command == "encrypt":
        print cipher(message, -shift)
    elif command == "decrypt":
        print cipher(message, shift)
    else:
        print "Unsupported command: {}".format(command)
        print usage()


if __name__ == "__main__":
    main() 

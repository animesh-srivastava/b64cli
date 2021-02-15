from argparse import ArgumentParser, ArgumentTypeError
from base64 import b64encode, b64decode
from pyperclip import copy


def string_to_boolean(value):
    """
    This is a misc function to assist argparse.
    This function takes in an argument and returns the equivalent
    Boolen value for it.
    """
    if isinstance(value, bool):
        return value
    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise ArgumentTypeError('Boolean value expected.')


def copy_to_clipboard(data):
    """
    Takes in a string and copies it to the clipboad.
    Uses default copy-paste mechanism at the backend
    """
    copy(data)
    print("Copied to clipboard!")


def encode(string, errors="backslashreplace",
           encoding="UTF-8", copy=True):
    """
    Takes in a string and some optional arguments and
    converts it to base64 encoded string.
    """
    try:
        string_bytes = string.encode(encoding=encoding, errors=errors)
    except UnicodeEncodeError:
        print("Could not encode string. Check if the string is in correct format and there are no illegal characters.")
        return False
    base64_bytes = b64encode(string_bytes)
    message = base64_bytes.decode(encoding)
    print("{0}".format(message))
    if copy:
        copy_to_clipboard(message)
    return message


def decode(string, errors="backslashreplace",
           encoding="UTF-8", copy=True):
    """
    Takes in an encoded string and some optional arguments and
    converts it back to human-readable string
    """
    base64_bytes = string.encode(encoding=encoding, errors=errors)
    string_bytes = b64decode(base64_bytes)
    try:
        message = string_bytes.decode(encoding)
    except UnicodeDecodeError:
        print("Could not decode string. Check if the input is a valid base64 string")
        return False
    print("{0}".format(message))
    if copy:
        copy_to_clipboard(message)
    return message


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="Base 64 CLI",
        description="A command line interface to encode and decode strings",
        epilog="Contributed by @animesh-srivastava"
    )

    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--encode",
                        "-e",
                        help="Encode input string")
    action.add_argument("--decode",
                        "-d",
                        help="Decode input string")
    parser.add_argument("-c",
                        "--copy",
                        type=string_to_boolean,
                        nargs="?",
                        const=True,
                        help="Copy to clipboard",
                        default=True)
    args = parser.parse_args()
    if args.encode:
        string = encode(args.encode,
                        copy=args.copy)
    elif args.decode:
        string = decode(args.decode,
                        copy=args.copy)

import argparse
import base64
import pyperclip


def copy_to_clipboard(data):
    """
    Takes in a string and copies it to the clipboad.
    Uses default copy-paste mechanism at the backend
    """
    pyperclip.copy(data)
    print("Copied to clipboard!")


def encode(string, errors="backslashreplace",
           encoding="UTF-8", copy=True, print_to_console=True):
    """
    Takes in a string and some optional arguments and
    converts it to base64 encoded string.
    """
    string_bytes = string.encode(encoding=encoding, errors=errors)
    base64_bytes = base64.b64encode(string_bytes)
    message = base64_bytes.decode(encoding)
    if print_to_console:
        print("{0}".format(message))
    if copy:
        copy_to_clipboard(message)
    return message


def decode(string, errors="backslashreplace",
           encoding="UTF-8", copy=True, print_to_console=True):
    """
    Takes in an encoded string and some optional arguments and
    converts it back to human-readable string
    """
    base64_bytes = string.encode(encoding=encoding, errors=errors)
    string_bytes = base64.b64decode(base64_bytes)
    message = string_bytes.decode(encoding)
    if print_to_console:
        print("{0}".format(message))
    if copy:
        copy_to_clipboard(message)
    return message


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Base 64 CLI",
        description="A command line interface to encode and decode strings",
        epilog="Contributed by @animesh-srivastava"
    )

    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--encode",
                        help="Encode input string")
    action.add_argument("--decode",
                        help="Decode input string")
    parser.add_argument("-p",
                        action="store_true",
                        help="Print to console",
                        default=True
                        )
    parser.add_argument("-c",
                        action="store_true",
                        help="Copy to clipboard",
                        default=True)
    args = parser.parse_args()
    if args.encode:
        string = encode(args.encode,
                        copy=args.c,
                        print_to_console=args.p)
    elif args.decode:
        string = decode(args.decode,
                        copy=args.c,
                        print_to_console=args.p)

import sys


def __out(message="", color=0, file=sys.stdout, **argk):
    print(f"\033[{color}m{message}\033[0m", file=file, **argk)


def cout(message="", color=0, **argk):
    __out(message=message, color=color, file=sys.stdout, **argk)


def cerr(message="", color=31, **argk):
    __out(message=message, color=color, file=sys.stderr, **argk)

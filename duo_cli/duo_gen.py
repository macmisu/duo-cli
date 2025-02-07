#!/usr/bin/env python3

import pyotp
import sys
import os.path


def main():
    if len(sys.argv) == 2:
        file_token = sys.argv[1]
    else:
        home = os.path.expanduser("~")
        file_token = os.path.join(home, ".config/duo/duotoken.hotp")

    try:
        f = open(file_token, "r+")
    except FileNotFoundError:
        sys.exit("Exit due to token file not found")
    except PermissionError:
        sys.exit("Exit due to permission denied to access token file")

    secret = f.readline()[0:-1]
    offset = f.tell()
    count = int(f.readline())

    print("secret", secret)
    print("count", count)

    hotp = pyotp.HOTP(secret)
    print("Code:", hotp.at(count))

    f.seek(offset)
    f.write(str(count + 1))
    f.close()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import pyotp
import pyqrcode
import json
import base64
import sys
import os.path


def main():
    home = os.path.expanduser("~")
    file_json = os.path.join(home, ".config/duo/response.json")
    file_token = os.path.join(home, ".config/duo/duotoken.hotp")

    try:
        with open(file_json, "r") as f:
            response = json.loads(f.read())["response"]
    except FileNotFoundError:
        sys.exit("Exit due to response JSON file not found")
    except PermissionError:
        sys.exit("Exit due to permission denied to access response JSON file")

    try:
        with open(file_token, "r") as f:
            counter = int(f.readlines()[1])
    except FileNotFoundError:
        sys.exit("Exit due to token file not found")
    except PermissionError:
        sys.exit("Exit due to permission denied to access token file")

    label = response["customer_name"]
    issuer = "Duo"
    # base32 encoded hotp secret, with the padding ("=") stripped.
    secret = (
        base64.b32encode(bytes(response["hotp_secret"], "utf-8"))
        .decode("utf-8")
        .replace("=", "")
    )
    qrdata = "otpauth://hotp/{label}?secret={secret}&issuer={issuer}&counter={counter}".format(
        label=label, secret=secret, issuer=issuer, counter=counter
    )
    qrcode = pyqrcode.create(qrdata)
    print(qrcode.terminal(quiet_zone=1))
    print(qrdata)


if __name__ == "__main__":
    main()

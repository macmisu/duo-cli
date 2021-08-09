#!/usr/bin/env python3

import pyotp
import requests
import base64
import json
import sys
import pathlib
import os.path


def main():
    if len(sys.argv) < 2:
        print("Usage: python duo_bypass.py <duo activation url>")
        sys.exit()

    qr_url = sys.argv[1]

    host = "api-%s" % (qr_url.split("/")[2].split("-")[1],)
    code = qr_url.rsplit("/", 1)[1]

    url = "https://{host}/push/v2/activation/{code}?customer_protocol=1".format(
        host=host, code=code
    )
    headers = {"User-Agent": "okhttp/2.7.5"}
    data = {
        "jailbroken": "false",
        "architecture": "armv7",
        "region": "US",
        "app_id": "com.duosecurity.duomobile",
        "full_disk_encryption": "true",
        "passcode_status": "true",
        "platform": "Android",
        "app_version": "3.23.0",
        "app_build_number": "323001",
        "version": "8.1",
        "manufacturer": "unknown",
        "language": "en",
        "model": "Pixel C",
        "security_patch_level": "2018-12-01",
    }

    r = requests.post(url, headers=headers, data=data)
    response = json.loads(r.text)

    try:
        secret = base64.b32encode(response["response"]["hotp_secret"].encode()).decode()
    except KeyError:
        print(response)
        sys.exit(1)

    print("secret", secret)

    # Generate 10 Otps!
    print("10 Next OneTime Passwords!")
    hotp = pyotp.HOTP(secret)
    for _ in range(10):
        print(hotp.at(_))

    home = os.path.expanduser("~")
    pathlib.Path(os.path.join(home, ".config/duo")).mkdir(parents=True, exist_ok=True)
    file_token = os.path.join(home, ".config/duo/duotoken.hotp")
    file_json = os.path.join(home, ".config/duo/response.json")

    f = open(file_token, "w")
    f.write(secret + "\n")
    f.write("0")
    f.close()

    with open(file_json, "w") as resp:
        resp.write(r.text)


if __name__ == "__main__":
    main()

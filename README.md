## Duo HOTP Password Generator

This is a little script I put together after I reverse engineered the Duo 2FA
Mobile App and figured out how their auth flow works. This can be ported into
probably a useful desktop app or chrome extention and can probably be used to
write bots for MIT Services that require auth.

### Usage

Install stuff,

```
pipx install git+https://github.com/macmisu/duo-cli
```
or
```
pip install git+https://github.com/macmisu/duo-cli
```

Grab the URL sent to you by email when adding the device (it might look like
https://m-XXXXXXXX.duosecurity.com/android/YYYYYYYYYYYYYYYYYYYY) and run:
```
./duo_activate.py {URL}
```

If everything worked you can then generate a code by running:

```
./duo_gen.py
```

Warning: These are HOTP tokens and generate codes increments a counter.  If you
get too far out of sync with the server it will stop accepting your codes.

```
./duo_export.py
```

Export the duo hotp secret as a QR code for inclusion in third-party hotp apps
like freeotp.

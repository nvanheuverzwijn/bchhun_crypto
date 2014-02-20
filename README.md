bchhun_crypto.pybchhun_crypto
=============

bchhun's encryption

Usage
-----
```
usage: bchhun_crypto.py [-h] [--decode] [STR]
    
bchhun's crypto

positional arguments:
  STR         the string to decode or encode. Pass '-' to read from stdin.

optional arguments:
  -h, --help  show this help message and exit
  --decode    decode STR
```

Exemple
-------
To encode a string

    $ ./bcchun_crypto string_to_encode
    Ll13225Ll13456Ll12996Ll11025Ll12100Ll10609Pc9025Ll13456Ll12321Pc9025Ll10201Ll12100Ll9801Ll12321Ll10000Ll10201
    $
    
To decode a string

    $ ./bchhun_crypto --decode Ll13225Ll13456Ll12996Ll11025Ll12100Ll10609Pc9025Ll13456Ll12321Pc9025Ll10201Ll12100Ll9801Ll12321Ll10000Ll10201
    string_to_encode
    $ 
    

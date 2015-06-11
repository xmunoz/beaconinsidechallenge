## [caesar](http://www.xmunoz.com/caesar/)
Encrypt and decrypt a string using a [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)!

## CLI Usage

The Ceaser Cipher tool can also be used as a command line tool, with a configurable shift value. Currently the shift is hard-coded to 3. Usage:

    python ceaser.py encrypt 'foo bar!' # outputs CLL YXO!
    python ceaser.py decrypt 'cll yxo!' # outputs FOO BAR!

## Web Usage
The web interface is a simple flask app with 3 endpoints: the home page, /encrypt and /decrypt.
[drag]: https://raw.githubusercontent.com/xmunoz/beaconinsidechallenge/master/screenshot.png

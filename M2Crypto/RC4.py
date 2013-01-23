"""M2Crypto wrapper for OpenSSL RC4 API.

Copyright (c) 1999-2003 Ng Pheng Siong. All rights reserved."""

from .__m2crypto import rc4_new, rc4_free, rc4_set_key, rc4_update

class RC4:

    """Object interface to the stream cipher RC4."""

    rc4_free = rc4_free

    def __init__(self, key=None):
        self.cipher = rc4_new()
        if key:
            rc4_set_key(self.cipher, key)

    def __del__(self):
        if getattr(self, 'cipher', None):
            self.rc4_free(self.cipher)

    def set_key(self, key):
        rc4_set_key(self.cipher, key)

    def update(self, data):
        return rc4_update(self.cipher, data)

    def final(self):
        return ''



import hashlib
import binascii

# Constants
class PKCS12(object):
    def SHA1_DIGEST_BLOCKLEN(self):
        return 64


    def SHA1_DIGEST_VALUELEN(self):
        return 20

    # Functions
    def PBKDF_Adjust(self, a, aOffset, b):
        x = (b[len(b) - 1] & 0xff) + (a[aOffset + len(b) - 1] & 0xff) + 1
        a[aOffset + len(b) - 1] = x & 0xff

        x = x >> 8

        for i in range(len(b) - 2, -1, -1):
            x = x + (b[i] & 0xff) + (a[aOffset + i] & 0xff)
            a[aOffset + i] = x & 0xff
            x = x >> 8


    def PBKDF_PKCS12v1(self, iteration, password, salt, keylen):
        v = self.SHA1_DIGEST_BLOCKLEN()
        u = self.SHA1_DIGEST_VALUELEN()
        r = iteration
        c = 0

        digest = bytearray(self.SHA1_DIGEST_VALUELEN())
        B = bytearray(self.SHA1_DIGEST_BLOCKLEN())
        key = bytearray(keylen)
        iv = bytearray(keylen)

        # Step 1
        Dlen = v
        D = bytearray(Dlen)

        for i in range(0, 64):
            D[i] = 1

        # Step 2
        Slen = v * int((len(salt) + v - 1) / v)
        S = bytearray(Slen)

        i = 0
        while (i != v * int((len(salt) + v - 1) / v)):
            S[i] = salt[i % len(salt)]
            i = i + 1

        # Step 3
        Plen = v * int((len(password) + v - 1) / v)
        P = bytearray(Plen)

        i = 0
        while (i != v * int((len(salt) + v - 1) / v)):
            P[i] = password[i % len(password)]
            i = i + 1

        # Step 4
        Ilen = Slen + Plen
        I = S + P

        # Step 5
        c = int((keylen + u - 1) / u)

        # Step 6
        for i in range(1, c + 1):
            # Step 6 - a
            sha1Alg = hashlib.sha1()
            sha1Alg.update(D)
            # sha1Alg.update(S)
            # sha1Alg.update(P)
            sha1Alg.update(I)

            digest = sha1Alg.digest()
            # print("- digest[1] : " + binascii.hexlify(digest).upper())

            for j in range(0, r - 1):
                sha1Alg = hashlib.sha1()
                sha1Alg.update(digest)
                digest = sha1Alg.digest()
                # print("- digest[" + str(j + 2) + "] : " +  binascii.hexlify(digest).upper())

            # Step 6 - b
            for k in range(0, self.SHA1_DIGEST_BLOCKLEN()):
                B[k] = digest[k % self.SHA1_DIGEST_VALUELEN()]

            # Strp 6 - c
            for j in range(0, int(Ilen / v)):
                self.PBKDF_Adjust(I, j * v, B)

            if (i == c):
                for j in range(0, keylen - ((i - 1) * u)):
                    key[(i - 1) * u + j] = digest[j]
            else:
                for j in range(0, self.SHA1_DIGEST_VALUELEN()):
                    key[(i - 1) * u + j] = digest[j]


        for i in range(0, 64):
            D[i] = 2

        # Step 2
        Slen = v * int((len(salt) + v - 1) / v)
        S = bytearray(Slen)

        i = 0
        while (i != v * int((len(salt) + v - 1) / v)):
            S[i] = salt[i % len(salt)]
            i = i + 1

        # Step 3
        Plen = v * int((len(password) + v - 1) / v)
        P = bytearray(Plen)

        i = 0
        while (i != v * int((len(salt) + v - 1) / v)):
            P[i] = password[i % len(password)]
            i = i + 1

        # Step 4
        Ilen = Slen + Plen
        I = S + P

        # Step 5
        c = int((keylen + u - 1) / u)

        # Step 6
        for i in range(1, c + 1):
            # Step 6 - a
            sha1Alg = hashlib.sha1()
            sha1Alg.update(D)
            # sha1Alg.update(S)
            # sha1Alg.update(P)
            sha1Alg.update(I)

            digest = sha1Alg.digest()
            # print("- digest[1] : " + binascii.hexlify(digest).upper())

            for j in range(0, r - 1):
                sha1Alg = hashlib.sha1()
                sha1Alg.update(digest)
                digest = sha1Alg.digest()
                # print("- digest[" + str(j + 2) + "] : " +  binascii.hexlify(digest).upper())

            # Step 6 - b
            for k in range(0, self.SHA1_DIGEST_BLOCKLEN()):
                B[k] = digest[k % self.SHA1_DIGEST_VALUELEN()]

            # Strp 6 - c
            for j in range(0, int(Ilen / v)):
                self.PBKDF_Adjust(I, j * v, B)

            if (i == c):
                for j in range(0, keylen - ((i - 1) * u)):
                    iv[(i - 1) * u + j] = digest[j]
            else:
                for j in range(0, self.SHA1_DIGEST_VALUELEN()):
                    iv[(i - 1) * u + j] = digest[j]
        return [key,iv]

    def REMOVE_PKCS7_PADDING(self,argBuf):
        buf = bytearray(argBuf)
        pos = len(buf) - 1

        val = buf[pos]

        while ((0x01 <= val) and (val <= 0x10)):
            buf[pos] = 0x00
            pos = pos - 1
            if (val != buf[pos]):
                break

        if (pos != len(buf) - 1):
            length = len(buf) - pos - 1
            buf = buf[0:len(buf) - length]

        return buf

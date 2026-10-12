import struct, zlib

data = open('challenge.png', 'rb').read()
stored_crc = struct.unpack('>I', data[29:33])[0]

matches = []
for w in range(1, 65536):
    chunk = bytearray(data[12:29])
    chunk[0:4] = struct.pack('>I', w)  
    if zlib.crc32(chunk) & 0xffffffff == stored_crc:
        matches.append(w)

print("Width matches found:", matches)

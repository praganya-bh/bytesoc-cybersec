import struct, zlib

raw = open('partial_decompressed.bin', 'rb').read()

width = 724
row_size = width * 3 + 1
usable_rows = len(raw) // row_size
raw = raw[:usable_rows * row_size]  

print(f"Building PNG: {width} x {usable_rows}")

def make_chunk(ctype, data):
    return (struct.pack('>I', len(data)) + ctype + data +
            struct.pack('>I', zlib.crc32(ctype + data) & 0xffffffff))

sig = b'\x89PNG\r\n\x1a\n'
ihdr_data = struct.pack('>IIBBBBB', width, usable_rows, 8, 2, 0, 0, 0)
ihdr = make_chunk(b'IHDR', ihdr_data)
idat = make_chunk(b'IDAT', zlib.compress(raw))
iend = make_chunk(b'IEND', b'')

open('reconstructed.png', 'wb').write(sig + ihdr + idat + iend)
print("Wrote reconstructed.png")


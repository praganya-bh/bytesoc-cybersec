import zlib

data = open('challenge.png', 'rb').read()
idat_positions = [0x25, 0x10031, 0x2003d, 0x30055, 0x40061, 0x5006d, 0x60079]
iend_pos = 0x6559f
boundaries = idat_positions + [iend_pos]

real_idat_data = b''
for i in range(len(idat_positions)):
    start = boundaries[i] + 4
    end = boundaries[i+1] - 8
    real_idat_data += data[start:end]

raw_deflate = real_idat_data[2:]  

d = zlib.decompressobj(-15)  
decompressed = d.decompress(raw_deflate)
decompressed += d.flush()

print("Decompressed:", len(decompressed))
row_size = 724 * 3 + 1
print("Full rows recovered:", len(decompressed) // row_size)
print("Leftover bytes:", len(decompressed) % row_size)

open('partial_decompressed.bin', 'wb').write(decompressed)
print("Saved to partial_decompressed.bin")
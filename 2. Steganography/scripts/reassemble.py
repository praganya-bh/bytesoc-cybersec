data = open('challenge.png', 'rb').read()

idat_positions = [0x25, 0x10031, 0x2003d, 0x30055, 0x40061, 0x5006d, 0x60079]
iend_pos = 0x6559f

boundaries = idat_positions + [iend_pos]

real_idat_data = b''
for i in range(len(idat_positions)):
    start = boundaries[i] + 4       
    end = boundaries[i+1] - 8       
    chunk_data = data[start:end]
    real_idat_data += chunk_data
    print(f"Chunk at {hex(boundaries[i])}: recovered {len(chunk_data)} bytes")

print("Total recovered IDAT payload:", len(real_idat_data))
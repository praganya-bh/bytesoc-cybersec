import struct

with open('challenge.png', 'rb') as f:
    data = bytearray(f.read())

data[20:24] = struct.pack('>I', 850) 

with open('challenge_fixed.png', 'wb') as f:
    f.write(data)

print("Patched. Wrote challenge_fixed.png")
import re

data = open('challenge.png', 'rb').read()

for marker in [b'IHDR', b'IDAT', b'IEND']:
    positions = [m.start() for m in re.finditer(marker, data)]
    print(marker, "found at offsets:", [hex(p) for p in positions])
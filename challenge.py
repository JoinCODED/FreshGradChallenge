def decrypt(encryped):
    return ''.join(chr(i) for i in encryped)

messages = [[97, 112, 112, 108, 121, 46, 106, 111, 105, 110, 99, 111, 100, 101, 100, 46, 99, 111, 109, 47, 106, 97, 100, 111, 100, 106, 111, 115, 100, 107, 110, 99, 106, 115, 111, 100]]

for msg in messages:
  print(decrypt(msg))
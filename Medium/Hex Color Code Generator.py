def rgb_to_hex(r, g, b):
  return ('#{:X}{:X}{:X}').format(r, g, b).lower()

red = int(input())
green = int(input())
blue = int(input())
print(rgb_to_hex(red, green, blue))
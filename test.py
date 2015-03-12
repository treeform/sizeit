from sizeit import get_size

# testing

import os

assert get_size("MyTestImages/1.png")  == ('image/png', (800, 600))
assert get_size("MyTestImages/2.png")  == ('image/png', (512, 512))

assert get_size("MyTestImages/1.jpeg") == ('image/jpeg', (2048, 1536))
assert get_size("MyTestImages/2.jpeg") == ('image/jpeg', (3000, 2357))


assert get_size("MyTestImages/1.gif")  == ('image/gif', (200, 200))

"""
for f in sorted(os.listdir("PngSuite")):
    if f.endswith(".png") and not f.startswith("x"):
        print f, get_size("PngSuite/" + f)
"""


### read image size without reading the whole image
import struct


def get_size(file_name):
    with open(file_name) as f:
        header = f.read(24)
        if header[0:8] == '\x89PNG\r\n\x1a\n':
            return png_size(header)
        elif header[0:6] == "GIF89a":
            return gif_size(header)
        elif header[0:2] == "\xff\xd8":
            return jpeg_size(f.read())
        else:
            return None


def png_size(header):
    # header is big-endian bytes
    # ?PNG? ???? 000? IHDR wwww hhhh"
    return ("image/png", struct.unpack(">II", header[16:24]))


def gif_size(header):
    # gif is little-endian bytes
    # GIF89a ww hh"
    return ("image/gif", struct.unpack("<HH", header[6:10]))


def jpeg_size(data):
    # jpeg is kind of hard because we need to
    # skip the thumb wich is a smaller image that appears first
    # look for FFCO JIFF header, use the largest one
    # jpeg is big-endian
    maxw = None
    maxh = None
    for index in range(0, len(data), 1):
        if data[index:index+2] == "\xFF\xC0":
            h,w = struct.unpack(">HH", data[index+5:index+9])
            if maxw is None or w*h > maxw*maxh:
                maxw = w
                maxh = h
    if maxw and maxh:
        return ("image/jpeg", (maxw, maxh))

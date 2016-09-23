from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

parser = argparse.ArgumentParser()

parser.add_argument("file")
parser.add_argument("-o", "--output")
parser.add_argument("--height", type = int, default=80)
parser.add_argument("--width", type = int, default=80)

args = parser.parse_args()
IMG = args.file
OUTPUT = args.output
HEIGHT = args.height
WIDTH = args.width


if __name__ == '__main__':
    img = Image.open(args.file)
    img = img.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt=''

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt +=
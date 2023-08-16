import argparse
import json
import sys
from PIL import Image, ImageDraw, ImageFont, ImageColor

BG_COLOR = '#effdca'
FG_COLOR = '#3f85f6' 
FONT = '../Roboto-Bold.ttf'
FONT_SIZE = 40


def main(argv):

    parser = argparse.ArgumentParser(
        description='Create Background Image')
    # parser.add_argument('-f', '--file', required=True)
    args = parser.parse_args(argv)

    img = Image.new('RGBA',(400,400),ImageColor.getrgb(BG_COLOR))
    d1 = ImageDraw.Draw(img)
    myPosition = (100, 100)
    content = 'Foobar'

    d1.text(myPosition, content,ImageColor.getrgb(FG_COLOR),font=ImageFont.truetype(FONT, FONT_SIZE))
    img.show()


if __name__ == "__main__":
    main(sys.argv[1:])


import argparse
import json
import sys
import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageColor
import yaml

# output_name = '../output_images/fg.png'

WIDESCREEN = (1280, 720)
ORIGINAL = (1280, 960)

FONT = 'resources/fonts/Roboto-Bold.ttf'
FONT = "resources/fonts/Tele Neo Office Bold.ttf"


def has_transparency(img):
    if img.info.get("transparency", None) is not None:
        return True
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True

    return False


def create_text_box(img, content, position, fg_color, font=FONT, font_size=20):
    d1 = ImageDraw.Draw(img)
    myPosition = position
    d1.text(myPosition, content, ImageColor.getrgb(fg_color), font=ImageFont.truetype(FONT, font_size))
    # img.show()
    return img


def create_image(config, image_dir='../', screen_size='original'):
    components = config['components']

    # Start with a transparent image
    if screen_size == 'widescreen':
        new_image = Image.new('RGBA', WIDESCREEN, (0, 0, 0, 0))
    else:
        new_image = Image.new('RGBA', ORIGINAL, (0, 0, 0, 0))

    for i in range(len(components)):
        comp = components[i]
        img_offset = (comp['x'], comp['y'])

        if (comp['type'] == 'text'):
            img = Image.new('RGBA', (comp['width'], comp['height']),
                            (0,0,0,0))
            content = comp['content']
            img = create_text_box(img, content, (0,0), '#ffffff')
            new_image.paste(img, img_offset)
        elif (comp['type'] == 'image'):
            filename = comp['location']
            foreground = Image.open(filename)
            foreground = ImageOps.contain(foreground,
                                          (comp['width'], comp['height']))  # resize

            if has_transparency(foreground):
                new_image.paste(foreground, img_offset, mask=foreground)
            else:
                new_image.paste(foreground, img_offset)
        else:
            continue

    return new_image


def create_bg_image(filename, screen_size='original'):
    # Start with background image
    new_image = Image.open(filename)

    if screen_size == 'widescreen':
        new_image = new_image.resize(WIDESCREEN)
    else:
        new_image = new_image.resize(ORIGINAL)

    return new_image


def main(argv):
    parser = argparse.ArgumentParser(
        description='Create Image')
    # parser.add_argument('-l', '--access_token', required=True)
    parser.add_argument('-b', '--background', required=False)
    args = parser.parse_args(argv)

    with open('resources/configs/tsystems1.json', 'r') as file:
        config = json.load(file)

    # TODO:  Grab this from the access-token room information
    screen_size = 'original'  # can be original/widescreen (1280 x 768, 1280x960)

    foreground = create_image(config)
    # foreground.show()
    foreground.save('tmp/fg.png','PNG')

    if(args.background):
        background = create_bg_image(args.background)
        # background.show()
        background.save('tmp/bg.png','PNG')

if __name__ == "__main__":
    main(sys.argv[1:])

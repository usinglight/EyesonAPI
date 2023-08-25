from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, font_filepath, font_size, color):
  font = ImageFont.truetype(font_filepath, size=font_size)
  img = Image.new("RGBA", font.getsize_multiline(text), (255,255,255))

  draw = ImageDraw.Draw(img)
  draw.multiline_text((0,0), text, font=font, fill=color)

  return img

def text_to_image_test():
    img = text_to_image("This is line 1\nThis is line 2\nThis is line 3", "/Users/stefansteinbauer/Github/EyesonAPI/EyesonAPIHelpers/Roboto-Bold.ttf", 14, (0,0,0)) 
    img.save("test.png")
import random
import string
from PIL import Image , ImageDraw , ImageFont , ImageFilter

#configuration 
CAPTCHA_LENGTH = 6
IMAGE_LENGTH = 160
IMAGE_BREADTH = 60
FONT_SIZE = 42
BACKGROUND_COLOR= (255,255,255)
TEXT_COLOR = (0,0,0)
NOISE_COLOR = (100,100,100)

def generate_random_text(length):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_captcha_image(text):
    image = Image.new('RGB',(IMAGE_LENGTH , IMAGE_BREADTH), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype('aerial.ttf',FONT_SIZE)
    except IOError:
        font = ImageFont.load_default()

# width and height of the text to be drawn
    text_bbox = draw.textbbox((0,0),text ,font=font)
    text_length = text_bbox[2] - text_bbox[0]
    text_breadth = text_bbox[3] - text_bbox[1]

    # Position of the text(X,Y)
    x = (IMAGE_LENGTH - text_length)/2
    y = (IMAGE_BREADTH - text_breadth)/2

    # Draw text

    draw.text((x,y) , text, font = font , fill = TEXT_COLOR)

    # Add some noise (dots)
    for _ in range(random.randint(100,300)):
        x1 = random.randint(0,IMAGE_LENGTH)
        y1 = random.randint(0,IMAGE_BREADTH)
        draw.point((x1,y1), fill = NOISE_COLOR)

    #add some noise (lines)
    for _ in range(random.randint(5,15)):
        x1 = random.randint(0,IMAGE_LENGTH)
        x2 = random.randint(0,IMAGE_LENGTH)
        y1 = random.randint(0,IMAGE_BREADTH)
        y2 = random.randint(0,IMAGE_BREADTH)
        draw.line(((x1,y1) ,(x2,y2)) , fill = NOISE_COLOR ,width =1)

    # avoid too strong filter
    image = image.filter(ImageFilter.EDGE_ENHANCE)

    return image

def main():
    # generate captcha text
    captcha_text = generate_random_text(CAPTCHA_LENGTH)
    print(f'generated captcha text: {captcha_text}')


     # Create CAPTCHA image
    captcha_image = create_captcha_image(captcha_text)

       # Save the image to a file
    captcha_image.save('CAPTCHA.png')

     # Optionally, display the image
    captcha_image.show()


if __name__ == '__main__':
    main()
     










  
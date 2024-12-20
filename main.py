from PIL import Image, ImageFilter, ImageDraw, ImageFont
from chiefkeef.ImageHandler import ImageHandler
from chiefkeef.ImageProcessor import ImageProcessor

def main():

    image = ImageHandler('image.jpg')
    image.change_size((200, 200))
    
    rezult_img  = ImageProcessor(image)
    rezult_img.add_filter()
    rezult_img.add_text((50,100), "3 variant", size = 15, color = 'black')

    rezult_img = image
    image.save_new('image2.jpg')

main()

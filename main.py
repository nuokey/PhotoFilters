from PIL import Image, ImageFilter, ImageOps

img = Image.open('img.png')

def crop_image():
	global img
	img_crop = img.crop((50, 50, 200, 200))
	img_crop.save('img_crop.png')

def rotate_image():
	global img
	img_rotate = img.rotate(30)
	img_rotate.save('img_rotate.png')

def blur_image():
	global img
	img_blur = img.filter(ImageFilter.BLUR)
	img_blur.save('img_blur.png')

def sharpen_image():
	global img
	img_sharpen = img.filter(ImageFilter.SHARPEN)
	img_sharpen.save('img_sharpen.png')

def contour_image():
	global img
	img_contour = img.filter(ImageFilter.CONTOUR)
	img_contour.save('img_contour.png')

def detail_image():
	global img
	img_detail = img.filter(ImageFilter.DETAIL)
	img_detail.save('img_detail.png')

def emboss_image():
	global img
	img_emboss = img.filter(ImageFilter.EMBOSS)
	img_emboss.save('img_emboss.png')

def smooth_image():
	global img
	img_smooth = img.filter(ImageFilter.SMOOTH)
	img_smooth.save('img_smooth.png')

def blue_image():
	global img
	blue_image = img
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			rgb = img.getpixel((x, y))
			blue = 255
			blue_image.putpixel((x, y), (rgb[0], rgb[1], blue))

	blue_image.save('image_blue.png')

def red_image():
	global img
	red_image = img
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			rgb = img.getpixel((x, y))
			red = 255
			red_image.putpixel((x, y), (red, rgb[1], rgb[2]))

	red_image.save('image_red.png')

def green_image():
	global img
	green_image = img
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			rgb = img.getpixel((x, y))
			green = 255
			green_image.putpixel((x, y), (rgb[0], green, rgb[2]))

	green_image.save('image_green.png')

def random_image():
	global img
	random_image = ImageOps.invert(img)
	random_image.save('random_image.png')

crop_image()
rotate_image()
blur_image()
sharpen_image()
detail_image()
smooth_image()
emboss_image()
blue_image()
red_image()
green_image()
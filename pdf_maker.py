from PIL import Image
import PyPDF2 as pypdf
import os

# image1 = Image.open(r'image_red.png')
# image2 = Image.open(r'image_green.png')
# image3 = Image.open(r'img_emboss.png')

# im1 = image1.convert('RGB')
# im2 = image2.convert('RGB')
# im3 = image3.convert('RGB')

imagelist = []

files = os.listdir()

for i in files:
    if i.endswith('.png'):
        imagelist.append(Image.open(i))

pdf_write = pypdf.PdfFileWriter()

pdf_write._addObject('img.png')

pdf_write.write(open('mergedimages.pdf', 'wb'))
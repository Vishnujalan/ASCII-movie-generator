import ascii_magic
import imgkit
import os
import cv2
from PIL import Image

#creating folders
os.mkdir('vid2img')
os.mkdir('img2ascii')
os.mkdir('ascii2jpg')


#opencv fn to read the video
vidcap = cv2.VideoCapture('got.mp4')
success,image = vidcap.read()
count = 0

#get fun is used to find the frames per second of the video
fps=float(vidcap.get(cv2.CAP_PROP_FPS))

while success:
    cv2.imwrite("vid2img\\frame%d.jpg" % count, image)         
    success,image = vidcap.read()
    #print('Read a new frame: ', success)
    count += 1

print("FRAMES SUCCESSFULLY READ...")

# img=Image.open("vid2img\\frame1.jpg")
# x,y=img.size
# wr=y/x
# print(wr)
wr=1.65

for i in range(count):

    my_art = ascii_magic.from_image_file('vid2img\\frame%d.jpg' %i, columns=100, width_ratio=wr, mode=ascii_magic.Modes.HTML)
    ascii_magic.to_html_file('img2ascii\\ascii%d.html' %i, my_art,additional_styles='background: #222;')

    path=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'
    config=imgkit.config(wkhtmltoimage=path)
    imgkit.from_file('img2ascii\\ascii%d.html' %i,'ascii2jpg\\fr%d.jpg' %i ,config=config)

frame=cv2.imread('ascii2jpg\\fr0.jpg')
ih, iw, il=frame.shape
fourcc=cv2.VideoWriter_fourcc(*'mp4v')
video=cv2.VideoWriter('asciiVideo2.mp4', fourcc, fps ,(iw, ih))

for i in range(count):
    image='ascii2jpg\\fr%d.jpg' %i
    video.write(cv2.imread(image))

cv2.destroyAllWindows()

video.release()












from PIL import Image
from pylab import *

#设置当前工作路径
#work_dir= "C:\Users\Administrator\Desktop\实心实验\Inquisit\叶容杉_差别阈限\"

#读取图片，灰度化，并转为数组
#for i in range(1,16)
im=array(Image.open("11.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("1"+"2"+".bmp")

im=array(Image.open("21.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("2"+"2"+".bmp")

im=array(Image.open("31.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("3"+"2"+".bmp")

im=array(Image.open("41.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("4"+"2"+".bmp")

im=array(Image.open("51.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("5"+"2"+".bmp")

im=array(Image.open("61.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("6"+"2"+".bmp")

im=array(Image.open("71.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("7"+"2"+".bmp")

im=array(Image.open("81.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("8"+"2"+".bmp")

im=array(Image.open("91.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("9"+"2"+".bmp")

im=array(Image.open("101.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("10"+"2"+".bmp")

im=array(Image.open("111.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("11"+"2"+".bmp")

im=array(Image.open("121.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("12"+"2"+".bmp")

im=array(Image.open("131.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("13"+"2"+".bmp")

im=array(Image.open("141.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("14"+"2"+".bmp")

im=array(Image.open("151.jpg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("15"+"2"+".bmp")

im=array(Image.open("161.jpeg").convert('L'))
image=(215/255)*im
out=Image.fromarray(uint8(image))
out.save("16"+"2"+".bmp")










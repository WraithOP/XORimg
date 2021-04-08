from PIL import Image

import optparse

parser=optparse.OptionParser()

parser.add_option("-f","--image1",dest="im1",help="Name of Image-1")
parser.add_option("-s","--image2",dest="im2",help="Name of Image-2")
parser.add_option("-o","--output",dest="out",help="Name of output Image file")
(option,argument)=parser.parse_args()


print("[!] Note Add extention also.")

pic1_name=option.im1
pic2_name=option.im2
out_name=option.out


pic1=Image.open(pic1_name)
print("[+] Reading pic1")  #finding the size of picture1 
pic2=Image.open(pic2_name)
print("[+] Reading pic2") #finding the size of picture2


'''
so that we can xor each and every coordinate of both the pictures
'''

x_cord_pic1=pic1.size[0]
y_cord_pic1=pic1.size[1]

newpic = Image.new('RGB',pic1.size) # Creating NEW image

for y in range(y_cord_pic1):
    for x in range(x_cord_pic1):
        pixel_1=pic1.getpixel((x,y))
        pixel_2=pic2.getpixel((x,y))
        newpixel =[]
        for p in range(len(pixel_1[:3])): #for all three values

            newpixel.append(pixel_1[p] ^ pixel_2[p]) # ^ --> use to xor two Values
        newpixel=tuple(newpixel)
        newpic.putpixel((x,y),newpixel)
print("[+] Xored successfully")
print("[+]  Successfully saved as "+out_name)
newpic.save(out_name)

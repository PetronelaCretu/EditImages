'''
Created on 10.02.2017
@author: Petronela Cretu
'''


from __future__ import print_function
from PIL import Image, ImageDraw, ImageFont

import os, sys

class EditImage():
    def __init__(self):
        self._image = None
        self._imageName = ''

    @property
    def image(self):
        return self._image
    
    @property
    def imageName(self):
        return self.imageName
    
    @image.setter
    def image(self, filePath):
        self._image, self._imageName = self.openImage(filePath)
        
        
    def openImage(self, imgName):
        try:
            return (Image.open(imgName), imgName)
        except IOError:
            print(imgName + ' error opening file')


    def displayImage(self, img):
        img.show()
        

    def resizeImg(self, img, imgName, picSize = (640, 427)):
        x, y =  img.size
        if x < y:
            z, t = picSize
            picSize = (t, z)
        img = img.resize(picSize)
        print(imgName)
        imgName = "D:\\" + imgName.split("\\")[-1]
        
        print(imgName)
        imgName = imgName.split(".")[0] + str(picSize) + "." + imgName.split(".")[1]
        img.save(imgName, "JPEG")
        return img, imgName

    def mergeImages(self, img1, img2):
        newImg = Image.blend(img1, img2, 1.0)
        newImg.save(img1.name + 'signed', "jpeg")
    
    def addTextToImage(self,img, name, text = None, color = (0,0,0), location = (0,0), size = 42):
        draw = ImageDraw.Draw(img)
        #ITCBLKAD.TTF
        fnt = ImageFont.truetype("C:/Windows/Fonts/PALSCRI.TTF", size)
        draw.text(location, "Petronella", color, font=fnt)
        img.save(name, 'JPEG')


def importImages(directory):
    listFilesPaths = list()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg"):
    #                 print(os.path.join(root, file))
                listFilesPaths.append(os.path.join(root, file))
    return listFilesPaths

if __name__ == '__main__':
    ei = EditImage()
    images = importImages("D:\\imgs")
    for name in images:
        img, name = ei.openImage(name)
        img, name = ei.resizeImg(img, name)
        x, y = img.size
        ei.addTextToImage(img, name, location=(x-120, y-40))
#       ei.displayImage(img)
    
    
    


        
        
'''
Created on 10.02.2017
@author: Petronela Cretu
'''

from PIL import Image, ImageDraw, ImageFont

import os


class EditImage(object):
    
    def __init__(self):
        self._image = None
        self._imageName = ''

    @property
    def image(self):
        return self._image
#     
    @property
    def imageName(self):
        return self._imageName
    
    @image.setter
    def image(self, filePath):
        self._image = Image.open(filePath)
        
    @imageName.setter
    def imageName(self,image):
        self._imageName = self.image.filename
            
   
    def displayImage(self, img):
        img.show()
        

    def resizeImg(self, picSize = (640, 427)):
        x, y = self.image.size
        if x < y:
            z, t = picSize
            picSize = (t, z)
        self._image = self._image.resize(picSize)

#         self.imageName = "D:\\" + self.imageName.split("\\")[-1]

        self._imageName = self._imageName.split(".")[0] + str(picSize) + "." + self._imageName.split(".")[1]
        self._image.save(self._imageName, "JPEG")
        

    def mergeImages(self, img1, img2):
        newImg = Image.blend(img1, img2, 1.0)
        newImg.save(img1.name + 'signed', "jpeg")
    
    def addTextToImage(self, text = None, color = (0,0,0), location = (0,0), size = 42):
        draw = ImageDraw.Draw(self.image)
        #ITCBLKAD.TTF
        fnt = ImageFont.truetype("C:/Windows/Fonts/PALSCRI.TTF", size)
        draw.text(location, text, color, font=fnt)
        self.image.save(self.imageName, 'JPEG')


def importImages(directory):
    listFilesPaths = list()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg"):
    #                 print os.path.join(root, file)
                listFilesPaths.append(os.path.join(root, file))
    return listFilesPaths

if __name__ == '__main__':
    ei = EditImage()
    images = importImages("D:\\imgs")
    for name in images:
        ei.image = name
        ei.imageName = ei.image
        ei.resizeImg((600, 400))
        x, y = ei.image.size
        ei.addTextToImage(text = "Your Name", color = (3,3,3), location=(x-120, y-40), size = 20)
#       ei.displayImage(img)
    


        
        

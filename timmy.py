from glob import glob
import sys
from PIL import Image, ImageFilter

#1
#def jpg2png(oldName,newName):
    #try:
        #Im = Image.open(oldName)
        #dotIndex = oldName.index(".")
        #newName = oldName[:dotIndex] + "-png2jpg" + oldName[dotIndex:]
        #Im.save(newName, "png")
        #print("image is saved as ", newName, "\n")
    #except FileNotFoundError as fnfe:
        #print(fnfe)

#def png2jpg(oldName,newName):
    #try:
        #Im = Image.open(oldName)
        #Im = Im.convert("RGB")
        #Im.save(newName, "jpeg")
        #dotIndex = oldName.index(".")
        #newName = oldName[:dotIndex] + "-png2jpg" + oldName[dotIndex:]
        #Im.save(newName, "jpeg")
        #print("image is saved as ", newName, "\n")
    #except FileNotFoundError as fnfe:
        #print(fnfe)
#2

#3
def rotateImg(imgName):
    try:
        img = Image.open(imgName)
        print("選轉選項: ")
        print("1. 左右翻轉")
        print("2. 上下翻轉")
        print("3. 旋轉90度")
        print("4. 旋轉180度")
        print("5. 旋轉270度")
        print("6. other")
        op1 = input("您要進行的操作:　")
        if op1 == "1":
            newIm =img.transpose(Image.FLIP_LEFT_RIGHT)
            str1 = "_flip_LR"
        elif op1 == "2":
            newIm =img.transpose(Image.FLIP_TOP_BOTTOM)
            str1 = "_flip_TB"
        elif op1 == "3":
            newIm =img.transpose(Image.ROTATE_90)
            str1 = "_rotate_90"
        elif op1 == "4":
            newIm =img.transpose(Image.ROTATE_180)
            str1 = "_rotate_180"
        elif op1 == "5":
            newIm =img.transpose(Image.ROTATE_270)
            str1 = "_rotate_270"
        elif op1 == "6":
            rotDegree = float(input("Rotate degree: "))
            newIm =img.rotate(rotDegree)
            str1 = "_rotate_" + str(rotDegree)
        dotIndex = imgName.index(".")
        newImgName = imgName[:dotIndex] + str1 + imgName[dotIndex:]
        newIm.save(newImgName)
        print("Rotated image is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print(fnfe)

#5
def resizeImg(imgName):
    try:
        img = Image.open(imgName)
        print("Current size (width, height)", img.size)
        newWidth = int(input("new width: "))
        ratio = float(newWidth) / img.size[0]
        newHeight = int(img.size[1] * ratio)
        resizeImg = img.resize( (newWidth, newHeight), Image.BILINEAR )
        print("new image size: ", resizeImg.size)
        dotIndex = imgName.index(".")
        newImgName = imgName[:dotIndex] + "_resized" + imgName[dotIndex:]
        resizeImg.save(newImgName)
        print("Resized img is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print(fnfe)

#7
def genThumbnail(imgName):
    try:
        img = Image.open(imgName)
        print("Current size (width, height)", img.size)
        newWidth, newHeight = map(int, input("請輸入縮圖尺寸: ").split())
        img.thumbnail((newWidth, newHeight))
        dotIndex = imgName.index(".")
        print(dotIndex)
        newImgName = imgName[:dotIndex] + "_thumbnail" + imgName[dotIndex:]
        img.save(newImgName)
        print("Thumbnail image is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print(fnfe)

#9
def applyFilter(imgName):
    try:
        img = Image.open(imgName)
        print("綠競選向")
        print("1.模糊")
        print("2.輪廓")
        print("3.細節增強")
        print("4.邊緣增強")
        print("5.深度邊緣增強")
        print("6.浮雕效果")
        print("7.邊緣訊息")
        print("8.平滑效果")
        print("9.深度平滑效果")
        print("A.銳利化效果")
        op1 = input("選擇要套用的濾淨")
        if op1 == "1":
            newImg =img.filter(ImageFilter.BLUR)
            str1 = "_BLUR"
        elif op1 == "2":
            newImg =img.filter(ImageFilter.CONTOUR)
            str1 = "_CONTOUR"
        elif op1 == "3":
            newImg =img.filter(ImageFilter.DETAIL)
            str1 = "_DETAIL"
        elif op1 == "4":
            newImg =img.filter(ImageFilter.EDGE_ENHANCE)
            str1 = "_EDGE_ENHANCE"
        elif op1 == "5":
            newImg =img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            str1 = "_EDGE_ENHANCE_MORE"
        elif op1 == "6":
            newImg =img.filter(ImageFilter.EMBOSS)
            str1 = "_EMBOSS"
        elif op1 == "7":
            newImg =img.filter(ImageFilter.FIND_EDGES)
            str1 = "_FIND_EDGES"
        elif op1 == "8":
            newImg =img.filter(ImageFilter.SMOOTH)
            str1 = "_SMOOTH"
        elif op1 == "9":
            newImg =img.filter(ImageFilter.SMOOTH_MORE)
            str1 = "_SMOOTH_MORE"
        elif op1 == "A":
            newImg =img.filter(ImageFilter.SHARPEN)
            str1 = "_SHARPEN"
        dotIndex = imgName.index(".")
        newImgName = imgName[:dotIndex] + str1 + imgName[dotIndex:]
        newImg.save(newImgName)
        print("Filtered img is saved as ", newImgName, "\n")
    except FileNotFoundError as fnfe:
        print(fnfe)

def showMenu():
    print("-------------------------------------------------------")
    print("1. 張單影像格式轉換")
    print("2. 批次處理目錄內同一種影像格式的所有影像進行格式轉換")
    print("3. 張單影像旋轉")
    print("4. 批次處理目錄內同一種影像格式的所有影像進行影像旋轉")
    print("5. 張單影像等比例縮放")
    print("6. 批次處理目錄內同一種影像格式的所有影像進行影像等比例縮放")
    print("7. 張單影像縮圖製作")
    print("8. 批次處理目錄內同一種影像格式的所有影像進行影像縮圖製作")
    print("9. 張單影像濾鏡套用")
    print("10.批次處理目錄內同一種影像格式的所有影像進行影像濾鏡套用")
    print("0.結束")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        while True:
            showMenu()
            op = input("選擇功能: ")
            #if op == "1":
                #if sys.argv[1] == "-jpg2png":
                    #jpg2png(sys.argv[1])
                #elif sys.argv[1] == "-png2jpg":
                    #png2jpg(sys.argv[1])
            if op == "3":
                rotateImg(sys.argv[1])
            elif op == "5":
                resizeImg(sys.argv[1])
            #elif op == "6":
                #if sys.argv[1] == "-all":
                    #imList = glob("*.[jJ][pP][Gg]")
                    #resizeImg(sys.argv[1])
            elif op == "7":
                genThumbnail(sys.argv[1])
            elif op == "9":
               applyFilter(sys.argv[1])
            elif op == "0":
                print("bye")
                break
    else:
        print("argument error")

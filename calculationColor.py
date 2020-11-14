import cv2
import numpy as np

# 240 x 320 camera

def cropImage(image,h=465,w=472):
    #greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    greyImage = image
    y=20
    x=20
    greyImage = greyImage[y:y+h, x:x+w]
    
    #########################____Quradrant2_____#############################
    greyImage = cv2.line(greyImage, (62,63), (74,63), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (68,57), (68,69), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (162,63), (174,63), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (168,57), (168,69), (0,255,0), 2)


    markPointQ1In1 = 68


    greyImage = cv2.line(greyImage, (62,163), (74,163), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (68,157), (68,169), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (162,163), (174,163), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (168,157), (168,169), (0,255,0), 2)

    #########################____Quradrant1_____#############################
    greyImage = cv2.line(greyImage, (312,63), (324,63), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (318,57), (318,69), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (412,63), (424,63), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (418,57), (418,69), (0,255,0), 2)

    greyImage = cv2.line(greyImage, (312,163), (324,163), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (318,157), (318,169), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (412,163), (424,163), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (418,157), (418,169), (0,255,0), 2)

    #########################____Quradrant3_____#############################
    greyImage = cv2.line(greyImage, (62,313), (74,313), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (68,307), (68,319), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (162,313), (174,313), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (168,307), (168,319), (0,255,0), 2)

    greyImage = cv2.line(greyImage, (62,413), (74,413), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (68,407), (68,419), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (162,413), (174,413), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (168,407), (168,419), (0,255,0), 2)

     #########################____Quradrant4_____#############################
    greyImage = cv2.line(greyImage, (312,313), (324,313), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (318,307), (318,319), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (412,313), (424,313), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (418,307), (418,319), (0,255,0), 2)

    greyImage = cv2.line(greyImage, (312,413), (324,413), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (318,407), (318,419), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (412,413), (424,413), (0,255,0), 2)
    greyImage = cv2.line(greyImage, (418,407), (418,419), (0,255,0), 2)

    
    
    

    cv2.imshow("CROP", greyImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    img = cv2.imread("0100RE2.jpg", cv2.IMREAD_COLOR)
    #img = cv2.line(img, (0,0), (400,400), (0,255,0), 5)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cropImage(img)

        
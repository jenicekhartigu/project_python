import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def nacti_display(filename):
    img = cv.imread(filename)

    print("Reading " + 'display.png')

    rows,cols,ch = img.shape
    pts1 = np.float32([[77,231],[813,0],[182,570],[940,323]])
    pts2 = np.float32([[0,0],[845,0],[0,355],[845,355]])
    M = cv.getPerspectiveTransform(pts1,pts2)
    dst = cv.warpPerspective(img,M,(845,355))

    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')

    plt.show()

def read_jpg_to_red(filename):
    try:
        jpg = cv.imread(filename)  # načteni jpg
        print("Reading " + filename)

        picture = cv.cvtColor(jpg, cv.COLOR_BGR2RGB) # převod do RGB
        red_part = cv.cvtColor(jpg, cv.COLOR_BGR2RGB) 
        white = np.ones(3)*255  # bílá
        current = np.zeros(3)

        # 
        for i in range(0,red_part.shape[0]):
            for j in range(0,red_part.shape[1]):
                current = red_part[i][j]  # aktualni pozice
                np.seterr(divide='ignore', invalid='ignore')
                tmp = current[0]/np.sum(current)
                if tmp < 0.5:
                    red_part[i][j] = white  # přepsani na bilou

        # vykresleni
        plt.figure(1) 
        plt.subplot(1,2,1) 
        plt.title('picture')
        plt.imshow(picture)

        plt.subplot(1,2,2) 
        plt.title('Red part')
        plt.imshow(red_part)

        plt.show() 

    except Exception as error:
        print('ERROR: ' + error.__str__())

    return None

if __name__ == '__main__':
    nacti_display('display.png')
    read_jpg_to_red('ball.jpg')

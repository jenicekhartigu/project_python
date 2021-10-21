import math
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def najdi_souradnice(filename):

    # Mouse callback function
    global click_list
    positions, click_list = [], []
    def callback(event, x, y, flags, param):
        if event == 1: click_list.append((x,y))
    cv.namedWindow('img')
    cv.setMouseCallback('img', callback)

    img = cv.imread(filename)

    # Mainloop - show the image and collect the data
    while True:
        cv.imshow('img', img)    
        # Wait, and allow the user to quit with the 'esc' key
        k = cv.waitKey(1)
        # If user presses 'esc' break 
        if k == 27: break        
    cv.destroyAllWindows()
    
    return click_list

def nacti_display(filename):
    click_list = najdi_souradnice(filename)

    img = cv.imread(filename)

    rows,cols,ch = img.shape
    #[[77,231],[813,0],[182,570],[940,323]]
    pts1 = np.float32(click_list)

    print(*click_list, sep = "\n")
    str1 = click_list[0][0] - click_list[2][0]
    str2 = click_list[0][1] - click_list[2][1]
    str3 = click_list[1][0] - click_list[0][0]
    str4 = click_list[0][1] - click_list[1][1]
    res1 = math.sqrt((str1**2)+(str2**2))
    res2 = math.sqrt((str3**2)+(str4**2))
    print (str(res1) + " " + str(res2))
    res1 = math.floor(res1)
    res2 = math.floor(res2)
    print (str(res1) + " " + str(res2))


    pts2 = np.float32([[0,0],[res2,0],[0,res1],[res2,res1]])
    M = cv.getPerspectiveTransform(pts1,pts2)
    dst = cv.warpPerspective(img,M,(res2,res1))

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
    #read_jpg_to_red('ball.jpg')
    #najdi_souradnice()
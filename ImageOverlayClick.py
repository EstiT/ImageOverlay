#Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document].
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).

#Stephenson, B. "Tutorial 2: Using Images with the SimpleGraphics Library" [PDF document].
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).


from SimpleGraphics import *  #import simple graphics 

def main(): #define main function
    bg=input("What background picture would you like to use?")
    gif=input("What picture would you like to overlay?")
    topPic=loadImage(gif) #load image
    halfW=int(getWidth(topPic)/2) #calculate half of the width of the topPic
    halfH=int(getHeight(topPic)/2)#calculate half of the hieght of the topPic
    x=0#set starting coordinates that are outside of range
    y=0#set starting coordinates that are outside of range

    print("Click somewhere in the window to choose where the image will go")
    #continue until user gives valid input
    while x<halfW or x>800-halfW or y<halfH or y>600-halfH: 
        #get the coordinates of the mouse position
        x,y=mousePos() 
        update() #update to run properly
        #continue while mouse is within simple graphics window and has not been pressed
        while not leftButtonPressed(): 
            update() #update to run properly
            if leftButtonPressed():
                #get coordinates of where the click was
                x,y=mousePos() 
                #if the click is outside of range (not enough room for the whole image to be displayed in the window)
                if x<halfW or x>800-halfW or y<halfH or y>600-halfH: 
                    print("That is not a valid coordinate, try again") #error messege 
                    
    images(bg,gif,x,y)



def images(bg,gif,x,y):
    bg=loadImage(bg) #load the background image
    topPic=loadImage(gif) 
    bgW=int(getWidth(bg)) #calculate the width of the background
    bgH=int(getHeight(bg)) #calculate the height of the background
    bgX = int(getWidth() / 2 - bgW / 2) #x coordinate for it to be centered
    bgY = int(getHeight() / 2 - bgH / 2)#y coordinate for it to be centered
    drawImage(bg, bgX,bgY) #display centered background

    topPicW = int(getWidth(topPic)) #get the width of topPic
    topPicH= int(getHeight(topPic)) #get the height of topPic
    NewImg=createImage(topPicW,topPicH) #make a new image that has the same dementions as topPic
 
     #run through every pixel in the image
    for x1 in range (0,topPicW): 
        for y1 in range (0,topPicH):
            r,g,b=getPixel(topPic,x1,y1) #get colours for each pixel
            r1,g1,b1=getPixel(bg,x+x1-int(topPicW/2), y+y1-int(topPicH/2)) #colours for each pixel from bg
        
            if not (r<=130 and g>=140 and b<=130): # if it is not green
                r=int((r+r1)/2) #get the average of the bg and topPic for red,
                g=int((g+g1)/2) #green
                b=int((b+b1)/2) #and blue
                putPixel(NewImg,x1,y1,r,g,b) #change the pixel colours to look transparent
     
    drawImage(NewImg,x-topPicW/2,y-topPicH/2) #draw the new transparent image 

main() 

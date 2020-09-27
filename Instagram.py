#ivri korem 2020
"""
description
"""

#init
#import
from tkinter import *
from PIL import Image, ImageTk

#defining vars
targetImg = 0
votes = 0
hasVoted= False

#setting gui
root = Tk()
root.title('Instagram')
#root.iconbitmap('###')

#setting imgs
img_1 = ImageTk.PhotoImage(Image.open('images/1.jpg'))
img_2 = ImageTk.PhotoImage(Image.open('images/2.jpg'))
img_3 = ImageTk.PhotoImage(Image.open('images/3.jpg'))
img_4 = ImageTk.PhotoImage(Image.open('images/4.jpg'))
img_5 = ImageTk.PhotoImage(Image.open('images/5.jpg'))
img_6 = ImageTk.PhotoImage(Image.open('images/6.jpg'))
img_7 = ImageTk.PhotoImage(Image.open('images/7.jpg'))
img_8 = ImageTk.PhotoImage(Image.open('images/8.jpg'))
img_9 = ImageTk.PhotoImage(Image.open('images/9.jpg'))
img_10 = ImageTk.PhotoImage(Image.open('images/10.jpg'))
img_11 = ImageTk.PhotoImage(Image.open('images/11.jpg'))
img_12 = ImageTk.PhotoImage(Image.open('images/12.jpg'))


imgList = [img_1,img_2,img_3,img_4,img_5,img_6,img_7,img_8,img_9,img_10,img_11,img_12]

currentImg = Label(image=imgList[targetImg])

def downScroll():
    global imgList
    global targetImg
    global currentImg

    #making bounderis
    if targetImg == 0:
        targetImg = len(imgList)

    currentImg.grid_forget()
    targetImg -= 1
    currentImg = Label(image= imgList[targetImg])
    currentImg.grid(row=1,column=2)

def upScroll():
    global imgList
    global targetImg
    global currentImg

    #making bounderis
    if targetImg == len(imgList) - 1 :
        targetImg = -1
    
    currentImg.grid_forget()
    targetImg += 1
    currentImg = Label(image= imgList[targetImg])
    currentImg.grid(row=1,column=2)

def Upvote():
    global hasVoted
    global votes
    global UpvoteButton
    global DownvoteButton

    votes += 1
    if hasVoted == False:
        hasVoted = True
        UpvoteButton.grid_forget()
        UpvoteButton = Button(root, text="👍", command=Downvote, padx=15, pady=15, state=DISABLED)
        UpvoteButton.grid(row=2, column=4)
    else:
        DownvoteButton.grid_forget()
        DownvoteButton = Button(root, text="👎", command=Downvote, padx=15, pady=15)
        UpvoteButton.grid_forget()
        UpvoteButton = Button(root, text="👍", command=Downvote, padx=15, pady=15, state=DISABLED)
        UpvoteButton.grid(row=2, column=4)
        DownvoteButton.grid(row=2, column=0)

def Downvote():
    global hasVoted
    global votes
    global UpvoteButton
    global DownvoteButton

    votes -= 1
    if hasVoted == False:
        hasVoted = True
        DownvoteButton.grid_forget()
        DownvoteButton = Button(root, text="👎", command=Downvote, padx=15, pady=15, state=DISABLED)
        DownvoteButton.grid(row=2, column=0)
    else:
        UpvoteButton.grid_forget()
        UpvoteButton = Button(root, text="👍", command=Downvote, padx=15, pady=15)
        DownvoteButton.grid_forget()
        DownvoteButton = Button(root, text="👎", command=Downvote, padx=15, pady=15, state=DISABLED)
        UpvoteButton.grid(row=2, column=4)
        DownvoteButton.grid(row=2, column=0)

#buttons
UpvoteButton = Button(root, text="👍", command=Upvote, padx=15, pady=15)
DownvoteButton = Button(root, text="👎", command=Downvote, padx=15, pady=15)
upButton = Button(root, text="⇑", command=upScroll, padx=25, pady=10)
downButton = Button(root, text="⇓", command=downScroll, padx=25, pady=10)

EmptyLabel = Label(root, text= "")

#displaying
upButton.grid(row=0, column=2)
currentImg.grid(row=1, column=2)
downButton.grid(row=2, column=2)
EmptyLabel.grid(row=2, column=1)
DownvoteButton.grid(row=2, column=0)
EmptyLabel.grid(row=2, column=3)
UpvoteButton.grid(row=2, column=4)


#setting mainloop
root.mainloop()
from conf import * # configuration file #
from tkinter import *
#import pygame
import os
import sys
import threading
import time
#import pyaes # a future implementation of encryption #
#HardCoded = "b2af8b7f3849a68f62749b3152e5f0ef" # hardcoded md5 to complete the password' (future implementation)#
pUsername = userName + ": " # append a ":" to the username #
WindowTitle = "doTXT PyMessenger" 
roomName = "" # The name of the room chosen by the user #
roomPath = "" # Path for the txt file #


# Method for receive the messages on the file #
def ReceiveData():
    linesRead = open(roomPath,"r")
    lengthFile = len(linesRead)
    while 1:
        newLength = len(linesRead)
        if newLength != lengthFile:
            a = 0
            for line in linesRead:
                a += 1
                if a == newLength:
                    message = line + "\n"
                    ChatLog.insert(END, message)
            lengthFile = newLength

# Method for joining the room #  
def JoinRoom():
    global baseMain
    global roomPath
    global roomName
    EntryBox.config(state=DISABLED)
    roomName = EntryBox.get("0.0",END).replace("\n","")
    if roomName != "":
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END,"Joining %s\n" % roomName)
        roomPath = sharedFolder + "\\" + roomName + ".txt"
        if os.path.exists(roomPath) != True:
            ChatLog.insert(END,"This room doesn't exist!\n")
            ChatLog.config(state=DISABLED)
        if os.path.exists(roomPath) == True:
            ChatLog.config(state=DISABLED)
            baseMain.destroy()
            connectedMessenger()       
    else:
        pass
    EntryBox.config(state=NORMAL)
    EntryBox.delete("0.0",END)
    
# Method for when enter is pressed on the first window (before joining a room) #    
def JoinRoomPress(event):
    JoinRoom()
    
# Method for when the "List rooms" buttom is pressed, it actually shows the available rooms #    
def PressActionList():
    ChatLog.config(state=NORMAL)
    ChatLog.delete("0.0",END)
    avalRooms = 0
    roomList = os.listdir(sharedFolder)
    ChatLog.insert(END, "Rooms available: \n")
    for room in roomList:
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(sharedFolder + "\\" + room)
		
        avalRooms += 1
        pRoom = room[:-4]
        ChatLog.insert(END, pRoom + " L.A.:" + time.ctime(mtime) + "\n" )
    ChatLog.insert(END,"\n")
    ChatLog.insert(END,"Total of %i rooms available!\n" % avalRooms) 
    ChatLog.insert(END,"--------------------------------------------\n\n")
    ChatLog.config(state=DISABLED)

# Method for disabling the entry, otherwise a new line would be added if enter is hold #   
def DisableEntry(event):
    EntryBox.config(state=DISABLED)
    
def connectedMessenger():
    try:
        # def getmixerargs():
            # pygame.mixer.init()
            # freq, size, chan = pygame.mixer.get_init()
            # return freq, size, chan
        
        # def initMixer():
            # BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
            # FREQ, SIZE, CHAN = getmixerargs()
            # pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)
            
        # def PlaySound():
            # pygame.init()

            # pygame.mixer.music.load("alertsound.wav")

            # pygame.mixer.music.play()
                
        def DisableEntry(event):
            EntryBox.config(state=DISABLED)
            
        def PressAction(event):
            SendMessage()
            
        def SendMessage():
            toSend = EntryBox.get("0.0",END)
            if toSend != "\n":
                EntryBox.config(state=NORMAL)
                EntryBox.delete("0.0",END)
                openFileWrite = open(roomPath,"a+")
                openFileWrite.write(pUsername + toSend + "\n")
                openFileWrite.close()
            else:
                pass
            
        def EmojiInsert(choice):
            if choice == 1:
                EntryBox.insert(END, ":cry: ")
            elif choice == 2:
                EntryBox.insert(END, ":joy: ")
            elif choice == 3:
                EntryBox.insert(END, ":cool: ")
            elif choice == 4:
                EntryBox.insert(END, ":aff: ")
            elif choice == 5:
                EntryBox.insert(END, ":joysmile: ")
            elif choice == 6:
                EntryBox.insert(END, ":smile: ")
            elif choice == 7:
                EntryBox.insert(END, ":xd: ")
            elif choice == 8:
                EntryBox.insert(END, ":thinking: ")
        
        def ReceiveData():
            try:
                ChatLog.config(state=NORMAL)
                linesRead = open(roomPath,"r").readlines()
                lengthFile = len(linesRead)
                for i in linesRead:
                    for word in i.split():
                        if word == ":cry:":
                            ChatLog.image_create(END, image = emoji1)
                        elif word == ":joy:":
                            ChatLog.image_create(END, image = emoji2)
                        elif word == ":cool:":
                            ChatLog.image_create(END, image = emoji3)
                        elif word == ":aff:":
                            ChatLog.image_create(END, image = emoji4)
                        elif word == ":joysmile:":
                            ChatLog.image_create(END, image = emoji5)
                        elif word == ":smile:":
                            ChatLog.image_create(END, image = emoji6)
                        elif word == ":xd:":
                            ChatLog.image_create(END, image = emoji7)
                        elif word == ":thinking:":
                            ChatLog.image_create(END, image = emoji8)
                        else:
                            if "pyimage" not in word:
                                ChatLog.insert(END, word + " ")
                    ChatLog.insert(END, "\n")
                ChatLog.see(END)
                while 1:
                    ChatLog.config(state=DISABLED)
                    linesRead = open(roomPath,"r").readlines()
                    newLength = len(linesRead)
                    if newLength != lengthFile:
                        ChatLog.config(state=NORMAL)
                        a = 1
                        for line in linesRead:
                            a += 1
                            if a == newLength :
                                for word in line.split():
                                    if word == ":cry:":
                                        ChatLog.image_create(END, image = emoji1)
                                    elif word == ":joy:":
                                        ChatLog.image_create(END, image = emoji2)
                                    elif word == ":cool:":
                                        ChatLog.image_create(END, image = emoji3)
                                    elif word == ":aff:":
                                        ChatLog.image_create(END, image = emoji4)
                                    elif word == ":joysmile:":
                                        ChatLog.image_create(END, image = emoji5)
                                    elif word == ":smile:":
                                        ChatLog.image_create(END, image = emoji6)
                                    elif word == ":xd:":
                                        ChatLog.image_create(END, image = emoji7)
                                    elif word == ":thinking:":
                                        ChatLog.image_create(END, image = emoji8)
                                    else:
                                        ChatLog.insert(END, word + " ")
                        print(type(base.focus_get()))
                        if base.focus_get() == None:   
                            PlaySound()   
                            PlaySound()
                        ChatLog.insert(END, "\n")
                        ChatLog.see(END)
                    ChatLog.config(state=DISABLED)
                    lengthFile = len(linesRead)
                    time.sleep(0.55)
            except:
                exitNotice = open(roomPath,"a+")
                exitNotice.write("SYSTEM: %s has left the chat!\n\n" % userName)
                sys.quit()

        RoomWindowTitle = WindowTitle + " ({})".format(roomName)            
        base = Tk()
        base.title(RoomWindowTitle)
        base.iconbitmap("icon.ico")
        base.geometry("400x500")
        base.resizable(width=FALSE, height=FALSE)

        ChatLog = Text(base, bd=1, bg="white", height="8", width="50", font="Arial",)
        ChatLog.insert(END, "Joined the room.\n\n")
        ChatLog.config(state=DISABLED)

        scrollbar = Scrollbar(base, command=ChatLog.yview)
        ChatLog['yscrollcommand'] = scrollbar.set
        
        emoji1 = PhotoImage(file = "emojis\\1.png")
        emoji2 = PhotoImage(file = "emojis\\2.png")
        emoji3 = PhotoImage(file = "emojis\\3.png")
        emoji4 = PhotoImage(file = "emojis\\4.png")
        emoji5 = PhotoImage(file = "emojis\\5.png")
        emoji6 = PhotoImage(file = "emojis\\6.png")
        emoji7 = PhotoImage(file = "emojis\\7.png")
        emoji8 = PhotoImage(file = "emojis\\8.png")

        SendButton = Button(base, font=30, text="Send", width="12", height=5,
                            bd=1, bg="#00ff00", activebackground="#003300",
                            command=SendMessage)
        Emoji1Button = Button(base,command = lambda: EmojiInsert(1))
        Emoji1Button.config(image=emoji1)
        
        Emoji2Button = Button(base,command = lambda: EmojiInsert(2))
        Emoji2Button.config(image=emoji2)
        
        Emoji3Button = Button(base,command = lambda: EmojiInsert(3))
        Emoji3Button.config(image=emoji3)
        
        Emoji4Button = Button(base,command = lambda: EmojiInsert(4))
        Emoji4Button.config(image=emoji4)
        
        Emoji5Button = Button(base,command = lambda: EmojiInsert(5))
        Emoji5Button.config(image=emoji5)
        
        Emoji6Button = Button(base,command = lambda: EmojiInsert(6))
        Emoji6Button.config(image=emoji6)
        
        Emoji7Button = Button(base,command = lambda: EmojiInsert(7))
        Emoji7Button.config(image=emoji7)
        
        Emoji8Button = Button(base,command = lambda: EmojiInsert(8))
        Emoji8Button.config(image=emoji8)
        
        EntryBox = Text(base, bd=2, bg="white",width="29", height="5", font="Arial")
        EntryBox.bind("<Return>", DisableEntry)
        EntryBox.bind("<KeyRelease-Return>", PressAction)

        scrollbar.place(x=376,y=6, height=420)
        ChatLog.place(x=6,y=6, height=420, width=370)
        EntryBox.place(x=128, y=463, height=30, width=265)
        SendButton.place(x=6, y=463, height=30)
        Emoji1Button.place(x=6, y=430, height=30, width=30)
        Emoji2Button.place(x=39, y=430, height=30, width=30)
        Emoji3Button.place(x=72, y=430, height=30, width=30)
        Emoji4Button.place(x=105, y=430, height=30, width=30)
        Emoji5Button.place(x=138, y=430, height=30, width=30)
        Emoji6Button.place(x=171, y=430, height=30, width=30)
        Emoji7Button.place(x=204, y=430, height=30, width=30)
        Emoji8Button.place(x=237, y=430, height=30, width=30)
        
        myThread = threading.Thread(target=ReceiveData)
        myThread.start()
        base.mainloop()
        myThread.join()
    
    except:
        sys.quit()

# Creates the window #
baseMain = Tk()
baseMain.title(WindowTitle)
baseMain.geometry("400x500")
baseMain.iconbitmap("icon.ico")
baseMain.resizable(width=FALSE, height=FALSE)

# Create the ChatLog that will show messages #
ChatLog = Text(baseMain, bd=2, bg="white", height="8", width="50", font="Arial",)
ChatLog.insert(END, "Welcome to doTXT!\n\nTo connect you can use 'List rooms' to list available\nrooms and enter the name of the room then click\n 'Join Room'.\n\nAny bugs please report on \n'ekosloswisky@gmail.com'\n\n----------------------------------------")
ChatLog.config(state=DISABLED)

# Link/Bind the Scrollbar to the Y-axis on the windows/entry box #
scrollbar = Scrollbar(baseMain, command=ChatLog.yview)
ChatLog['yscrollcommand'] = scrollbar.set

# Set the Buttons
JoinRoomButton = Button(baseMain, font=30, text="Enter Room", width="12", height=5,
                    bd=1, bg="#00ff00", activebackground="#003300",
                    command=JoinRoom)
ListRoomsButton = Button(baseMain, font=30, text="List Rooms", width="12", height=5,
                    bd=1, bg="#ff0000", activebackground="#cc0000",
                    command=PressActionList)
# Create Entry Box #
EntryBox = Text(baseMain, bd=2, bg="white",width="29", height="5", font="Arial")
EntryBox.bind("<Return>", DisableEntry)
EntryBox.bind("<KeyRelease-Return>", JoinRoomPress)

# Place all the widgets on the windows)
scrollbar.place(x=376,y=6, height=425)
ChatLog.place(x=6,y=6, height=425, width=370)
EntryBox.place(x=125, y=435, height=60, width=270)
JoinRoomButton.place(x=6, y=469, height=30)
ListRoomsButton.place(x=6, y=434, height=30)

if __name__ == "__main__":
    baseMain.mainloop()
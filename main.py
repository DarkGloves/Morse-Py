##########
# IMPORT #
##########

import morseEncode
from moduleDownloader import getmodules 
getmodules('customtkinter','clipboard', 'pillow', pipver=3)
import clipboard
from customtkinter import *
from PIL import Image

#######
# GUI #
#######

#Create main window
root = CTk()
root.geometry('450x700')
root.iconbitmap('icon.ico')
root.minsize(400, 600)
#Config rows/columns
root.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
root.columnconfigure((0,1), weight=1)
root.title('Morse Encoder/Decoder - DarkGloves')

#Import images
clipboardImg = CTkImage(light_image=Image.open('clipboard.png'))

#Widgets
title = CTkLabel(root,text='MORSE\nENCODER', font=('Terminal', 90, 'bold'), anchor='nw')
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
label1 = CTkLabel(root, text='Input your text / morse code here:', font=('Arial', 17))
label1.grid(row=1, column=0, columnspan=2, pady=10)
entry = CTkEntry(root, height=50, font=('Arial', 18))
entry.grid(row=2, column=0, columnspan=2, sticky='ew', padx=10)
label2 = CTkLabel(root, text= 'Morse code:', font= ('Arial', 17))
label2.grid(row=3, column=0, columnspan=2, sticky='s')
morseLabel = CTkLabel(master=root, fg_color=('Black', "gray20"),corner_radius=30, font=('Arial', 20))
morseLabel.grid(row=4, column=0, columnspan=2, padx=15)
copyButton1 = CTkButton(root, text='Copy To Clipboard', fg_color=('Black', "gray20"), hover_color='gray30', command=lambda : clipboard.copy(morseLabel.cget('text')), image=clipboardImg, compound = 'left')
copyButton1.grid(row=5, column=0, columnspan=2, sticky='new', padx=20)
label3 = CTkLabel(root, text='ASCII code:', font=('Arial', 17))
label3.grid(row=6, column=0, columnspan=2, sticky='s')
textLabel = CTkLabel(master=root, fg_color=('Black', "gray20"),corner_radius=30, font=('Arial', 20))
textLabel.grid(row=7, column=0, columnspan=2, padx=15)
copybutton2 = CTkButton(root, text='Copy To Clipboard', fg_color=('Black', "gray20"), hover_color='gray30', command=lambda : clipboard.copy(textLabel.cget('text')), image=clipboardImg, compound = 'left')
copybutton2.grid(row=8, column=0, columnspan=2, sticky='new', padx=20)

#Create function that auto-refreshes the labels
def autoupdate():
    entryVar = entry.get()
    morseLabel.configure(text = str(morseEncode.encode(entryVar)))
    textLabel.configure(text = str(morseEncode.decode(entryVar)))
    root.after(100, autoupdate)

#Active function
autoupdate()

#Launch
root.mainloop()
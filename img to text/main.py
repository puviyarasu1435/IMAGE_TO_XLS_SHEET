#  Name: puviyarasu p                                             
#  date: 20-10-2020                                               
#  subject: image to text                                         
#_____________________________________________________________________________________________________________
import tkinter as tk
import xlrd
import datetime
import xlwt
from xlutils.copy import copy
from tkinter import *
from tkinter import filedialog
import pytesseract       
from PIL import Image   
text = ""
def xlswrite(text1):
    book=xlrd.open_workbook("Book1.xls")
    s=book.sheet_by_index(0)
    maxrow=s.nrows
    global text
    for i in range(maxrow):
        textchange.config(text =s.row_values(i))
    books=copy(book)
    workbook=books.get_sheet(0)
    workbook.write(maxrow,0,str(datetime.datetime.now()))
    workbook.write(maxrow,1,text1)
    books.save("Book1.xls")
def imagetotext(filename):
    img = Image.open(filename)                               
    pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'   
    result = pytesseract.image_to_string(img)     
    with open('abc.txt',mode ='w') as file:      
                    file.write(result) 
                    xlswrite(result)


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    imagetotext(filename)

root = tk.Tk()
root.geometry('500x500')

button = tk.Button(root, text='Open', command=UploadAction)
button.pack(side = TOP, pady = 10)
textchange = Label(root,text = "geeksforgeeks")  
textchange.pack() 
root.mainloop()
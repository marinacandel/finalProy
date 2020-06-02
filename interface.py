from tkinter import * 
from PIL import ImageTk, Image 
from tkinter import filedialog 
from tkinter import messagebox as MessageBox
from prediccion import predict # importo el archivo prediccion.py
import os 

root = Tk() 
 
root.resizable(width=True, height=True)
root.title("Detectar Imagenes con redes neuronales")
root.iconbitmap("neuronal.ico")

def Traje_de(Direccion_Archivo):
    traje=predict(Direccion_Archivo)
    MessageBox.showinfo("RESULTADO", "ES UN TRAJE DE: "+traje) # título, mensaje
def openfn(): 
    #delimito el tipo de archivo
    filename = filedialog.askopenfilename(title='Abrir',filetype=(("Imagenes JPG","*.jpg"),("Imagenes JPEG","*.jpeg")))
    return filename 
def borrar():
    panel.delete(1.0,END)
def open_img(): 
    x = openfn() 
    img = Image.open(x) 
    img = img.resize((250, 250), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(img) 
    panel = Label(root, image=img) 
    panel.image = img 
    panel.pack()
    label1 = Label(root,text=x).pack()
    Traje_de(x)
    btn2 = Button(root, text='BORRAR',command=borrar).pack()

label = Label(root,text="TRABAJO REALIZADO POR MARINA CANAZA DELGADO").pack()
btn = Button(root, text='Abrir Imagen', command=open_img).pack()


root.mainloop() 

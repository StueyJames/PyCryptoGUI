from tkinter import *
import sys
from Crypto.Cipher import AES
import base64
import os

def encryption(privateInfo):
    BLOCK_SIZE = 16
    PADDING = '{'

    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))

    secret = os.urandom(BLOCK_SIZE)
    print('Secret key:', secret)

    cipher = AES.new(secret)

    encoded = EncodeAES(cipher, privateInfo)
    print('Cipher Text:', encoded.decode('UTF-8'))

root = Tk()
labelfont = ('times', 20, 'bold')
widget = Label(root, text='AES Encryption')
widget.config(bg='black', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=30)
widget.pack(expand=YES, fill=BOTH)

def fetch():
    encryption("%s" % ent.get('1.0', END+'-1c'))




ent = Text(root)
ent.insert('1.0', 'Type or Paste (Ctrl+V) \nYour Secret Message Here \nAfter Deleting This Text')
ent.config(width=20, height=10)
ent.pack(side=TOP, fill=X)
ent.focus()
ent.config(font=('courier', 15, 'normal'))



widget = Button(text='Encrypt', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='gumby')
widget.config(bd=8, relief=RAISED)
widget.config(bg='dark green', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
widget.config(command=fetch)

class StdoutRedirector(object):

    def __init__(self, text_area):
        self.text_area = text_area

    def write(self, str):
        self.text_area.insert(END, str)
        self.text_area.see(END)



text = Text()
text.config(font=('courier', 15, 'normal'))
text.config(width=20, height=10)
text.pack(expand=YES, fill=BOTH)
text.insert('1.0', 'Highlight and Ctrl+C To Copy\n\n')


sys.stdout = StdoutRedirector(text)




mainloop()
root.mainloop()

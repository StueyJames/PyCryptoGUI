from tkinter import *
from Crypto.Cipher import AES
import sys
import base64
import codecs

def decrypt(key, encryptedString):

    PADDING = '{'
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).decode('utf-8').rstrip(PADDING)
    try:
        cipher = AES.new(key)
        decoded = DecodeAES(cipher, encryptedString)
        print('Secret Message:', decoded)
    except:
        print("Error in decoding the secret message")

root = Tk()
labelfont = ('times', 20, 'bold')
widget = Label(root, text='AES Decryption')
widget.config(bg='black', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=30)
widget.pack(expand=YES, fill=BOTH)






ent = Text()
ent.insert('1.0', "Paste (Ctrl+V) Your Secret key Here \nWithout The b' and Final Single Quote \nAfter Deleting This Text")
ent.config(width=30, height=3)
ent.pack(side=TOP, fill=X)
ent.focus()




text = Text()
text.insert('1.0', 'Paste (Ctrl+V) Your Cypher Text Here \nAfter Deleting This Text')
text.config(width=30, height=3)
text.pack(expand=YES, fill=BOTH)


def decryption():
    key = ("%s" % ent.get('1.0', END+'-1c'))
    encoded_string = ("%s" % text.get('1.0', END+'-1c'))
    decrypt(codecs.escape_decode(key)[0], encoded_string)



widget = Button(text='Decrypt', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='gumby')
widget.config(bd=8, relief=RAISED)
widget.config(bg='dark green', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
widget.config(command=decryption)

class StdoutRedirector(object):

    def __init__(self, text_area):
        self.text_area = text_area

    def write(self, str):
        self.text_area.insert(END, str)
        self.text_area.see(END)




plain = Text()
plain.config(font=('courier', 15, 'normal'))
plain.config(width=30, height=12)
plain.pack(expand=YES, fill=BOTH)
plain.insert('1.0', 'Highlight and Ctrl+C To Copy:\n\n')

sys.stdout = StdoutRedirector(plain)



mainloop()
root.mainloop()

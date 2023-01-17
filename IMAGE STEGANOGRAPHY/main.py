                             #Image Steganography Using Tkinter in Python
                                        #By: Fady Maged Fakhry
                             ############################################



#Modules Import:
################

from tkinter import *             #import everything from Tkinter Library (Standard Interface GUI tool in Python)
from tkinter import messagebox    #to pop-up messages during runtime
import tkinter.filedialog         #to deal with files and file extensions
from PIL import Image             #import images module from the pillow.The PIL opens, manipulates and saves many different forms of images.
from PIL import ImageTk           #used to create and modify Tkinter photoimage from PIL images.
import os                         #to create and remove directory
from io import BytesIO



class Image_Steganography:

    #Main Window Function
    #####################
    def main(self, main_window):

        # Initializing the main window of Python Image Steganography Project.
        main_window.title("Image Steganography By Fady Maged")
        main_window.geometry('500x500')
        main_window.configure(bg='#e3f4a2')

        main_window_frame = Frame(main_window, height=200, width=500, bg='#e3f4a2')
        main_window_frame.place(x=0, y=0)

        main_window_title = Label(main_window_frame, text="Fadoud's Image Steganograohy!", bg='#e3f4a2', font=("Goudy Stout", 9))
        main_window_title.place(x=50, y=20)

        # encode button variable creates the encode button using the command lambda: self.
        encode_btn = Button(main_window_frame,text="ENCODE", bg='#e3f4f2', font=("Goudy Stout", 9),
                            command = lambda: self.encode_frame1(main_window_frame))
        encode_btn.place(x=50, y=80)

        # decode button variable creates the decode button using the command lambda: self.
        decode_btn = Button(main_window_frame,text="DECODE", bg='#e3f4f2', font=("Goudy Stout", 9),
                            command = lambda: self.decode_frame1(main_window_frame))
        decode_btn.place(x=320, y=80)
        #NOTE:  lambda : used to pass data to the callback function.


    #Return To Previous Menu Window Function
    ########################################
    def back_to_prv(self, current_frame):

        current_frame.destroy()
        self.main(main_window)


    #Encode Frame 1 Function
    ########################
    def encode_frame1 (self,prev_frame):
        prev_frame.destroy()

        enc_frame = Frame(main_window,width=500,height=500, bg='#e3f4a2')
        enc_frame.place(x=0, y=0)

        enc_lbl = Label(enc_frame, text="Select Image To Hide Text Into" ,font=("Goudy Stout", 9), bg='#e3f4a2')
        enc_lbl.place(x=50, y=20)

        select_btn =Button(enc_frame,text="SELECT", bg='#e3f4f2', font=("Goudy Stout", 9),
                            command = lambda: self.encode_frame2(enc_frame))
        select_btn.place(x=200, y=80)

        back_btn = Button(enc_frame,text="Back", bg='#e3f4f2', font=("Goudy Stout", 9),
                            command = lambda: self.back_to_prv(enc_frame))
        back_btn.place(x=320, y=400)

    #Decode Frame 1 Function
    ########################
    def decode_frame1 (self,prev_frame):
        prev_frame.destroy()

        dec_frame = Frame(main_window,width=500,height=500, bg='#e3f4a2')
        dec_frame.place(x=0, y=0)

        enc_lbl = Label(dec_frame, text="Select Image With Hidden Text" ,font=("Goudy Stout", 9), bg='#e3f4a2')
        enc_lbl.place(x=50, y=20)

        select_btn =Button(dec_frame,text="SELECT", bg='#e3f4f2', font=("Goudy Stout", 9),
                            command = lambda: self.decode_frame2(dec_frame))
        select_btn.place(x=200, y=80)

        back_btn = Button(dec_frame,text="Back", bg='#e3f4f2', font=("Goudy Stout", 9),
                            command = lambda: self.back_to_prv(dec_frame))
        back_btn.place(x=320, y=400)

    #Encoding Frame 2 Function
    ##########################
    def encode_frame2 (self,prev_frame):
        myfile = tkinter.filedialog.askopenfilename\
            (filetypes=([('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')]))
        prev_frame.destroy()
        current_frame = Frame(main_window, width=500, height=500, bg='#e3f4a2')
        current_frame.place(x=0, y=0)
        if not myfile:
            messagebox.showerror("Error!!" ,"No File Was Selected !")
        else:
            my_img = Image.open(myfile)
            img_to_enc = my_img.resize((300, 200))
            img_to_enc = ImageTk.PhotoImage(img_to_enc)
            _lbl_1 = Label(current_frame, text='Selected Image',font=("Goudy Stout", 9), bg='#e3f4a2')
            _lbl_1.place(x=150, y=20)
            img_lbl=Label(current_frame, image= img_to_enc, border='4', background='black')
            img_lbl.image = img_to_enc
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = my_img.size
            img_lbl.place(x=100, y=50)

            _lbl_2 = Label(current_frame, text='Enter Your Message!', font=("Goudy Stout", 9), bg='#e3f4a2')
            _lbl_2.place(x=120, y=320)

            textbox = Text(current_frame, width=33, height=3,border='4' )
            textbox.place(x=120, y=350)
            msg_to_enc = textbox.get("1.0", "end-1c")

            encode_btn = Button(current_frame, text='Encode',
                                command=lambda: [self.enc_fun(textbox, my_img), self.back_to_prv(current_frame)])
            encode_btn.config(font=("Goudy Stout", 9), bg='#e3f4f2')
            encode_btn.place(x=80, y=430)

            cancel_btn = Button(current_frame, text='Cancel',
                                command=lambda:  self.back_to_prv(current_frame))
            cancel_btn.config(font=("Goudy Stout", 9), bg='#e3f4f2')
            cancel_btn.place(x=320, y=430)

    # Function to Enter Hidden Text
    ###############################
    def enc_fun(self,text_a,myImg):
        data = text_a.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","Kindly enter text in TextBox")
        else:
            newImg = myImg.copy()
            self.encode_enc(newImg, data)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newImg.size
            messagebox.showinfo("Success","Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")


    #Decoding Frame 2 Function
    ##########################
    def decode_frame2(self, prev_frame):
        myfile = tkinter.filedialog.askopenfilename\
            (filetypes=([('png', '*.png'), ('jpeg', '*.jpeg'), ('jpg', '*.jpg'), ('All Files', '*.*')]))
        prev_frame.destroy()
        current_frame = Frame(main_window,width=500,height=500, bg='#e3f4a2')
        current_frame.place(x=0, y=0)
        if not myfile:
            messagebox.showerror("Error!!" ,"No File Was Selected !")
        else:
            my_img = Image.open(myfile,'r')
            img_to_enc = my_img.resize((300, 200))
            img_to_enc = ImageTk.PhotoImage(img_to_enc)
            _lbl_1 = Label(current_frame, text='Selected Image',font=("Goudy Stout", 9), bg='#e3f4a2')
            _lbl_1.place(x=150, y=20)
            img_lbl=Label(current_frame, image= img_to_enc, border='4', background='black')
            img_lbl.image = img_to_enc
            img_lbl.place(x=100, y=50)

            _lbl_2 = Label(current_frame, text='The Hidden Message is:', font=("Goudy Stout", 9), bg='#e3f4a2')
            _lbl_2.place(x=110, y=320)

            back_btn = Button(current_frame, text='BACK',
                                command=lambda:  self.back_to_prv(current_frame))
            back_btn.config(font=("Goudy Stout", 9), bg='#e3f4f2')
            back_btn.place(x=210, y=450)


            hidden_data = self.decode(my_img)

            textbox = Text(current_frame, width=33, height=3,border='4')
            textbox.insert(INSERT,hidden_data)
            textbox.configure(state='disabled')
            textbox.place(x=120, y=350)

    # Function to Decode Data
    #########################
    def decode(self, image):
        image_data = iter(image.getdata())
        data = ''
        while (True):
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] + image_data.__next__()[:3]]
            # string of binary data
            binary_str = ''
            for i in pixels[:8]:
                   if i % 2 == 0:
                     binary_str += '0'
                   else:
                     binary_str += '1'

            data += chr(int(binary_str, 2))
            if pixels[-1] % 2 != 0:
                return data

    # Function to Generate Data
    ###########################
    def generate_Data(self, data):
        # list of binary codes of given data
        new_data = []

        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data

    # Function to Modify The Pixels of Image
    ########################################
    def modify_Pix(self, pix, data):
        dataList = self.generate_Data(data)
        dataLen = len(dataList)
        imgData = iter(pix)
        for i in range(dataLen):
            # Extracting 3 pixels at a time
            pix = [value for value in imgData.__next__()[:3] +
                   imgData.__next__()[:3] +
                   imgData.__next__()[:3]]

            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pix[j] % 2 != 0):
                     if (pix[j] % 2 != 0):
                         pix[j] -= 1
                elif (dataList[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1

            if (i == dataLen - 1):
                if (pix[-1] % 2 == 0):
                     pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]

    # Function to Enter the Data Pixels In Image
    ############################################
    def encode_enc(self, newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modify_Pix(newImg.getdata(), data):

            # Putting modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1









main_window = Tk()
obj = Image_Steganography()
obj.main(main_window)
main_window.mainloop()

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy
#load the trained model to classify sign
from keras.models import load_model
model = load_model('traffic_classifier.h5')

#dictionary to label all traffic signs class.
classes = { 1: 'Tốc độ tối đa cho phép (20km/h)',
            2: 'Tốc độ tối đa cho phép (30km/h)',
            3: 'Tốc độ tối đa cho phép (50km/h)',
            4: 'Tốc độ tối đa cho phép (60km/h)',
            5: 'Tốc độ tối đa cho phép (70km/h)',
            6: 'Tốc độ tối đa cho phép (80km/h)',
            7: 'Hết hạn chế tốc độ tối đa (80km/h)',
            8: 'Tốc độ tối đa cho phép (100km/h)',
            9: 'Tốc độ tối đa cho phép (120km/h)',
            10: 'Cấm vượt',
            11: 'Cấm ô tô tải vượt',
            12: 'Giao nhau với đường ưu tiên',
            13: 'Đường ưu tiên',
            14: 'Chú ý nhường đường',
            15: 'Stop',
            16: 'Đường cấm',
            17: 'Cấm phương tiện từ 3.5 tấn',
            18: 'Cấm đi ngược chiều',
            19: 'Nguy hiểm chưa xác định',
            20: 'Chỗ ngoặt nguy hiểm bên trái',}

#initialise GUI
top=tk.Tk()
top.geometry('700x500')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = numpy.argmax(model.predict(image), axis=-1)[0]
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#011638', text=sign) 

def show_classify_button(file_path):
    classify_b=Button(top,text="NHẬN DẠNG",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="TẢI ẢNH LÊN",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="NHẬN DẠNG BIỂN BÁO GIAO THÔNG",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()

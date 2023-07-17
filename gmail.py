#import module

from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import smtplib
import ssl
from email.message import EmailMessage

def send_base():
    to_snd = To.get()
    subject_snd = Subject.get()
    content_snd = Content.get()
    
    try:
        email_sender = 'rashijain1710@gmail.com'
        email_password = 'aqqnlmcvllgpgdvv'
        email_receiver=str(to_snd)
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = str(subject_snd)
        em.set_content(str(content_snd))
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            messagebox.showinfo('Success',"Email Sent Successfully")
    except:
        messagebox.showinfo('Error',"Something wrong happened")
    my_wind.destroy()
    
def send():
    global To ,Subject, Content, Canvas1,my_wind
    my_wind=Tk()
    my_wind.title("Gmail Application")
    my_wind.geometry("{0}x{1}+0+0".format(my_wind.winfo_screenwidth(),my_wind.winfo_screenheight()))
    my_wind.overrideredirect(True)
    same=True
    n=1.75
# Adding a background image
    background_image =Image.open("mailbg1.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
    
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(background_image)
    Canvas1 = Canvas(my_wind)
    Canvas1.create_image(750,340,image = img)      
    Canvas1.config(bg="black",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)  
    headingFrame1 = Frame(my_wind,bg="#BCD2E8",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Compose", bg='black', fg='#BCD2E8', font=('Forte',45))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(my_wind,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #To
    lb1 = Label(labelFrame,text="To            :", bg='black', fg='#BCD2E8', font=('Forte',25))
    lb1.place(relx=0.05,rely=0.25, relheight=0.12)
    To = Entry(labelFrame,font=('Courier New Baltic',18))
    To.place(relx=0.3,rely=0.25, relwidth=0.62, relheight=0.12)
        
    #Subject
    lb2 = Label(labelFrame,text="Subject     :", bg='black', fg='#BCD2E8', font=('Forte',25))
    lb2.place(relx=0.05,rely=0.47, relheight=0.12)
    Subject = Entry(labelFrame,font=('Courier New Baltic',18))
    Subject.place(relx=0.3,rely=0.47, relwidth=0.62, relheight=0.12)
        
    #Content
    lb3 = Label(labelFrame,text="Content    :", bg='black', fg='#BCD2E8', font=('Forte',25))
    lb3.place(relx=0.05,rely=0.7, relheight=0.12)   
    Content = Entry(labelFrame,font=('Courier New Baltic',18))
    Content.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.12)
        
        
    #Send Button
    SubmitBtn = Button(my_wind,text="SEND",bg='#BCD2E8', fg='black', font=('Forte',25),command=send_base)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    #Quit Button
    quitBtn = Button(my_wind,text="Quit",bg='#BCD2E8', fg='black', font=('Forte',25),command=my_wind.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    my_wind.mainloop()
send()


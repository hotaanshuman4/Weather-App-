from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()

        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
#weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=57cf265c5238183d92b90e67279cc6ab"
        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")

#searchbox
root=Canvas(root,width=4500,height=3500)
root.pack()
image=PhotoImage(file='C:\\Users\\91797\\OneDrive\\Documents\\OneDrive\\Desktop\\weather\\image\\Copy of search.PNG')
root.create_image(0,0,anchor =NW,image=image)

textfield=tk.Entry(root,justify='center',width=17,font=('poppins',25,'bold'),bg='#404040',border=0,fg='white')
textfield.place(x=50,y=25)
textfield.focus()

Search_icon=PhotoImage(file="C:\\Users\\91797\\OneDrive\\Documents\\OneDrive\\Desktop\\weather\\image\\Copy of search_icon.PNG")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor='hand2',bg='#404040',command=getWeather)
myimage_icon.place(x=378,y=10)

#logo
logo_image=PhotoImage(file="C:\\Users\\91797\\OneDrive\\Documents\\OneDrive\\Desktop\\weather\\image\\Copy of logo.PNG")
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#clock
clock=Label(root,font=('Helvetica',23,'bold'))
clock.place(x=680,y=20)
name=Label(root,font=('Arial',15,'bold'))
name.place(x=680,y=80)


#bottombox
Frame_image=PhotoImage(file='C:\\Users\\91797\\OneDrive\\Documents\\OneDrive\\Desktop\\weather\\image\\Copy of box.PNG')
frame_myimage=Label(image=Frame_image)
frame_myimage.place(x=40,y=390)

#label
label1=Label(root,text='WIND',font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label1.place(x=100,y=360)

label2=Label(root,text='HUMIDITY',font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label2.place(x=230,y=360)

label3=Label(root,text='DESCRIPTION',font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label3.place(x=420,y=360)


label4=Label(root,text='PRESSURE',font=('Helvetica',15,'bold'),fg='white',bg='#1ab5ef')
label4.place(x=650,y=360)
 

t=Label(font=('arial',70,'bold'),fg='#ee666d')
t.place(x=400,y=150)
c=Label(font=('arial',15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=110,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=260,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=470,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=680,y=430)

root.mainloop()
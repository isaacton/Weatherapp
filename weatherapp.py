import tkinter as tk
from tkinter import font

HEIGHT = 600
WIDTH = 700

def test_fuction(entry):
    print("this is the entry:", entry)
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# 0fac85e23b60aba869697617c3f79411

def get_weather(city):
    weather_key = "0fac85e23b60aba869697617c3f79411"
    url = "api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "Q": "city", "units": "imperial"}
    response = response.get(url, params=params)
    weather = response.json()

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="landscape.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1)

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor = "n")

entry = tk.Entry(frame, font=40,)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get weather", font=40, command =lambda: test_fuction(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=40)
label.place(relwidth=1, relheight=1)

root.mainloop()
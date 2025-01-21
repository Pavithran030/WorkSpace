from gtts import gTTS
import os
from tkinter import *
from tkinter import messagebox
import speech_recognition as sr

def text_to_speech():
    text = text_entry.get("1.0", "end-1c")
    language = accent_entry.get()
    if len(text) <= 1 or len(language) <= 0:
        messagebox.showerror(message="Enter required details")
        return     
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("text.mp3")
    os.system("mpg123 "+"text.mp3")

def speech_to_text(): 
    recorder = sr.Recognizer()
    try:
        duration = int(duration_entry.get())
    except:
        messagebox.showerror(message="Enter the duration")
        return
    messagebox.showinfo(message="Speak into the microphone and wait after finishing the recording")  
    with sr.Microphone() as mic: 
        recorder.adjust_for_ambient_noise(mic)
        audio_input = recorder.listen(mic, duration=duration)   
        try:                        
            text_output = recorder.recognize_google(audio_input)
            messagebox.showinfo(message="You said:\n "+text_output)       
        except:
            messagebox.showerror(message="Couldn't process the audio input.")

def list_languages():
    # Placeholder for listing supported languages
    pass

window = Tk()
window.geometry("500x300")
window.title("Convert Speech to text and text to Speech: PythonGeeks")
title_label = Label(window, text="Convert Speech to text and text to Speech: PythonGeeks").pack()

text_label = Label(window, text="Text:").place(x=10, y=20)
text_entry = Text(window, width=30, height=5)
text_entry.place(x=80, y=20)

accent_label = Label(window, text="Accent:").place(x=10, y=110)
accent_entry = Entry(window, width=26)
accent_entry.place(x=80, y=110)

duration_label = Label(window, text="Duration:").place(x=10, y=140)
duration_entry = Entry(window, width=26)
duration_entry.place(x=80, y=140)

button1 = Button(window, text='List languages', bg='Turquoise', fg='Red', command=list_languages)
button1.place(x=10, y=190)

button2 = Button(window, text='Convert Text to Speech', bg='Turquoise', fg='Red', command=text_to_speech)
button2.place(x=130, y=190)

button3 = Button(window, text='Convert Speech to Text', bg='Turquoise', fg='Red', command=speech_to_text)
button3.place(x=305, y=190)

window.mainloop()

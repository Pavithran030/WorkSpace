import tkinter as tk
import customtkinter as ctk
import io
from PIL import Image, ImageTk, UnidentifiedImageError
from CTkMessagebox import CTkMessagebox
from authtokens import API_URL, headers
import requests

# Initialize the main window
gen = ctk.CTk()
gen.geometry("580x740")
gen.title("Text to Image")

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

global pht, pil_image
pil_image = None

# Function to generate an image based on the prompt
def generate():
    global pht, pil_image, prompt
    prompt = promptbox.get().strip()  # Get and strip whitespace from the prompt

    if not prompt:
        CTkMessagebox(title="Info", message="Please enter a prompt to generate an image.")
        return

    # Function to make the request to the API
    def query(payload):
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            return response
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            CTkMessagebox(title="Error", message="Failed to reach the API. Please try again later.")
            return None

    # Make the API call
    response = query({"inputs": prompt})

    # Check if the response is successful and contains valid data
    if response and response.status_code == 200:
        try:
            image_bytes = response.content
            pil_image = Image.open(io.BytesIO(image_bytes))  # Attempt to open the image

            # Resize the image for display
            image = pil_image.resize((396, 396), Image.LANCZOS)
            photo = ctk.CTkImage(light_image=image, dark_image=image, size=(396, 396))
            pht = photo

            # Update the label to show the image
            img.configure(image=photo)
            img.image = photo
        except UnidentifiedImageError:
            CTkMessagebox(title="Error", message="The received data is not a valid image.")
        except Exception as e:
            print(f"Error while processing image: {e}")
            CTkMessagebox(title="Error", message="An unexpected error occurred while processing the image.")
    else:
        error_message = f"Failed to generate image: {response.status_code}" if response else "No response received."
        CTkMessagebox(title="Error", message=error_message)

# Function to download the generated image
def download():
    global pil_image
    if pil_image:
        try:
            pil_image.save('generatedimage.png')
            CTkMessagebox(title="Success", message="Image has been saved as 'generatedimage.png'.")
        except Exception as e:
            print(f"Error saving image: {e}")
            CTkMessagebox(title="Error", message="Failed to save the image. Please try again.")
    else:
        CTkMessagebox(title="Info", message="Your image hasn’t been generated yet.")

# UI Layout
body = ctk.CTkFrame(gen, width=500, height=680, corner_radius=20)
body.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

l1 = ctk.CTkLabel(body, text='Text to Image', font=("Arial Black", 20), fg_color='transparent')
l1.place(x=180, y=10)

message = ctk.CTkLabel(body, text='Enter the prompt:', font=("Arial Black", 13), fg_color='transparent')
message.place(x=50, y=60)

promptbox = ctk.CTkEntry(body, placeholder_text='Describe the image', font=("Arial Black", 11), width=400)
promptbox.place(x=50, y=90)

lgbut = ctk.CTkButton(body, text='Generate', command=generate, font=("Arial Black", 13),fg_color='#06a603', hover_color="#045201", width=400)
lgbut.place(x=50, y=135)

img = ctk.CTkLabel(body, text="Your image will show up here once it’s generated.",font=("Arial Black", 13), height=396, width=396, bg_color="#1A1919", fg_color='transparent')
img.place(x=50, y=180)

dlbut = ctk.CTkButton(body, text='Download', command=download, font=("Arial Black", 15), height=40,fg_color='#06a603', hover_color="#045201", width=400)
dlbut.place(x=50, y=600)

gen.mainloop()

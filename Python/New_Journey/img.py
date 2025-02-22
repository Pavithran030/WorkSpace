# import tkinter as tk
# import customtkinter as ctk
# import io
# from PIL import Image,ImageTk
# from CTkMessagebox import CTkMessagebox
# from authtokens import API_URL,headers
# import requests
# import matplotlib.pyplot as plt


# gen = ctk.CTk()
# gen.geometry("580x740")
# gen.title("Text to Image")

# ctk.set_appearance_mode("system")
# ctk.set_default_color_theme("green")
 
 
# global pht, pil_image
# pil_image=""

# def generate():
#     global pht, pil_image , prompt
#     prompt = promptbox.get()
#     def query(payload):
#         response = requests.post(API_URL, headers=headers, json=payload)
#         return response.content
    
#     if prompt:
#         image_bytes = query({
#         "inputs": prompt,
#     })
#     else :
#         CTkMessagebox(title="Info", message="Please enter a prompt to generate an image.")
#         return

#     try:
#         pil_image = Image.open(io.BytesIO(image_bytes))

#         image = pil_image.resize((396, 396), Image.LANCZOS)
#         photo = ctk.CTkImage(light_image=image, dark_image=image, size=(396, 396))
#         pht = photo
       
#         img.configure(text="")
#         img.configure(image=photo) 
        
#     except Exception as e:
#         print(f"Error: {e}")

# def download():
#     global pil_image
#     if pil_image:
#         pil_image.save('generatedimage.png')
#     else:
#         CTkMessagebox(title="Info", message="Your image hasn’t been generated yet.")

# body= ctk.CTkFrame(gen, width=500, height=680, corner_radius=20)
# body.place(relx=0.5, rely=0.5,anchor=tk.CENTER)
 
 
# l1=ctk.CTkLabel(body, text='text to image',font=("Arial Black",20) ,fg_color='transparent')
# l1.place(x=180, y=10)


# message=ctk.CTkLabel(body, text='Enter the prompt : ',font=("Arial Black",13) ,fg_color='transparent')
# message.place(x=50,y=60)

# promptbox=ctk.CTkEntry(body,placeholder_text='describe the image ',font=("Arial Black",11) ,width=400)
# promptbox.place(x=50,y=90)


# lgbut=ctk.CTkButton(body, text='Generate',command=generate,font=("Arial Black",13) ,fg_color='#06a603',hover_color="#045201",width=400)
# lgbut.place(x=50,y=135)


# img = ctk.CTkLabel(body,text="""Your image will show up here once it’s generated.""",font=("Arial Black",13) ,height=396, width=396,bg_color="#1A1919",fg_color='transparent')
# img.place(x=50, y=180)


# dlbut=ctk.CTkButton(body, text='download',command=download,font=("Arial Black",15),height=40 ,fg_color='#06a603',hover_color="#045201",width=400)
# dlbut.place(x=50,y=600)

# gen.mainloop()

import pandas as pd
from scipy import stats

# Load the dataset
file_path = 'D:\\Download .Hack\\Student_Marks.csv'
data = pd.read_csv(file_path)

# Step 1: Create two groups based on the number of courses
group1 = data[data['number_courses'] <= 4]['Marks']  # Students with 4 or fewer courses
group2 = data[data['number_courses'] > 4]['Marks']   # Students with more than 4 courses

# Step 2: Perform an independent two-sample t-test
t_statistic, p_value = stats.ttest_ind(group1, group2)

# Step 3: Output the results
print(f"T-statistic: {t_statistic:.4f}")
print(f"P-value: {p_value:.4f}")

# Step 4: Conclusion based on p-value
alpha = 0.05  # Common threshold for significance
if p_value < alpha:
    print("There is a significant difference between the means of the two groups.")
else:
    print("There is no significant difference between the means of the two groups.")

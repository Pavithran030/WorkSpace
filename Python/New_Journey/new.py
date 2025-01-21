# Import required libraries
import torch
from diffusers import DiffusionPipeline
from PIL import Image

# Load the diffusion model (make sure it's available locally or can connect)
pipe = DiffusionPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell").to("cuda")  # Use "cpu" if GPU is not available

# Define the prompt
prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"

# Generate the image
image = pipe(prompt).images[0]

# Display the generated image
image.show()  # This will open the image in the default image viewer

# Optionally save the image
image.save('generated_image.png')
print("Image saved as 'generated_image.png'.")

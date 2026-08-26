import base64
import ollama

# Path to your image
image_path = r"c:\aitests\image.png"

# Read the image file and encode it to base64
with open(image_path, "rb") as image_file:
  image_data = base64.b64encode(image_file.read()).decode("utf-8")

# Send the request to Ollama using a vision model (like llava)
response = ollama.chat(
    model="llava",
    messages=[
        {
            "role": "user",
            "content": "What is written on this image? Transcribe all text.",
            "images": [image_data],
        }
    ],
)

# Print the model's response
print(response["message"]["content"])

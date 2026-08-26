import ollama
from pypdf import PdfReader

# 1. Extract text from PDF
reader = PdfReader("document.pdf")
file_text = ""
for page in reader.pages:
    file_text += page.extract_text()

# 2. Pass text into Gemma 4 via Ollama
response = ollama.generate(
    model="gemma4",
    prompt=f"Analyze the following text and give me a summary:\n\n{file_text}"
)

print(response['response'])

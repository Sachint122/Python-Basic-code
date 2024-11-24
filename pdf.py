import PyPDF2
import io
from PIL import Image

# Open the PDF file in binary mode
pdf_file = open('image.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# Get the first page of the PDF
page = pdf_reader.getPage(0)

# Extract the image from the page
xObject = page['/Resources']['/XObject'].getObject()
for obj in xObject:
    if xObject[obj]['/Subtype'] == '/Image':
        size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
        data = xObject[obj].getData()
        image = Image.frombytes('RGB', size, data)

# Convert the image to text using OCR
text = pytesseract.image_to_string(image, lang='eng')

# Print the extracted text
print(text)

# Close the PDF file
pdf_file.close()

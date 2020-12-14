import pyttsx3
import PyPDF2
book = open('testpdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
reader = pyttsx3.init()
for num in range(pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    reader.say(text)
    reader.runAndWait()

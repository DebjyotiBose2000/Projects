import pyttsx3
import PyPDF2

book = open('java.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("Total Number of Pages in the Book is:",pages)
n = eval(input("Enter the Page no. from where You are Want to Listen:"))
g = pyttsx3.init()

for i in range(n,pages):
    page = pdfReader.getPage(i)
    txt = page.extractText()
    g.say(txt)
    g.runAndWait()
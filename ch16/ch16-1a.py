from PyPDF2 import PdfFileReader
import os

pdf_path = os.getcwd()+"/PDF/Python海龜繪圖.pdf"
pdfReader = PdfFileReader(pdf_path)
for pageNo in range(0, pdfReader.numPages):
    page = pdfReader.getPage(pageNo)
    print(page.extractText())

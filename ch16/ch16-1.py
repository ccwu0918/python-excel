from PyPDF2 import PdfFileReader
import os

pdf_path = os.getcwd()+"/PDF/Python海龜繪圖.pdf"
pdfReader = PdfFileReader(pdf_path)
numberOfPages = pdfReader.numPages
print("頁數1:", numberOfPages)
numberOfPages = pdfReader.getNumPages()
print("頁數2:", numberOfPages)
info = pdfReader.getDocumentInfo()
print("作者:", info.author)
print("標題:", info.title)
print("製作者:", info.producer)

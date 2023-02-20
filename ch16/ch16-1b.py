from PyPDF2 import PdfFileReader, PdfFileWriter
import os

pdf_path = os.getcwd()+"/PDF/Python海龜繪圖.pdf"
pdf_output = os.getcwd()+"/PDF/Python海龜繪圖2.pdf"
pdfReader = PdfFileReader(pdf_path)
pdfWriter = PdfFileWriter()
page1 = pdfReader.getPage(0).rotateClockwise(90)
pdfWriter.addPage(page1)
with open(pdf_output, "wb") as fp:
    pdfWriter.write(fp)

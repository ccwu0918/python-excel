from PyPDF2 import PdfFileReader, PdfFileWriter
import os

pdf_output = os.getcwd()+"/PDF/Python海龜繪圖3.pdf"
pdfReader1 = PdfFileReader(os.getcwd()+"/PDF/Python海龜繪圖_p1.pdf")
pdfReader2 = PdfFileReader(os.getcwd()+"/PDF/Python海龜繪圖_p2.pdf")
pdfReader3 = PdfFileReader(os.getcwd()+"/PDF/Python海龜繪圖_p3.pdf")
pdfWriter = PdfFileWriter()
page1 = pdfReader1.getPage(0)
pdfWriter.addPage(page1)
page2 = pdfReader2.getPage(0)
pdfWriter.addPage(page2)
page3 = pdfReader3.getPage(0)
pdfWriter.addPage(page3)
with open(pdf_output, "wb") as fp:
    pdfWriter.write(fp)


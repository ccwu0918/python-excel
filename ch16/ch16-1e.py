from PyPDF2 import PdfFileReader, PdfFileWriter
import os

pdf_path = os.getcwd()+"/PDF/Python海龜繪圖.pdf"
watermark_path = os.getcwd()+"/PDF/Python海龜繪圖_浮水印.pdf"
pdf_output = os.getcwd()+"/PDF/Python海龜繪圖4.pdf"
watermarkReader = PdfFileReader(watermark_path)
watermarkpage = watermarkReader.getPage(0)
pdfReader = PdfFileReader(pdf_path)
pdfWriter = PdfFileWriter()
for pageNo in range(pdfReader.getNumPages()):
    page = pdfReader.getPage(pageNo)
    page.mergePage(watermarkpage)
    pdfWriter.addPage(page)
with open(pdf_output, "wb") as fp:
    pdfWriter.write(fp)


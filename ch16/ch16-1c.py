from PyPDF2 import PdfFileReader, PdfFileWriter
import os

pdf_path = os.getcwd()+"/PDF/Python海龜繪圖.pdf"
pdfReader = PdfFileReader(pdf_path)
fname = os.path.splitext(os.path.basename(pdf_path))[0]
for pageNo in range(pdfReader.getNumPages()):
    pdfWriter = PdfFileWriter()
    page = pdfReader.getPage(pageNo)
    pdfWriter.addPage(page)
    outputfname = "PDF/"+fname+"_p"+str(pageNo+1)+".pdf"
    with open(outputfname, "wb") as fp:
        pdfWriter.write(fp)
        print("分割建立PDF檔:", outputfname)

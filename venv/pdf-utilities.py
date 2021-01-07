import PyPDF2
import sys
import os

def rotateClockWise(pdfFilePath,outFile,direction='clockwise',angle=90):
    with open(pdfFilePath, 'rb') as pdfFile:
        print(f'Manipulate pdf {pdfFilePath}')
        reader = PyPDF2.PdfFileReader(pdfFilePath)
        page = reader.getPage(0)
        if direction == 'clockwise':
            page.rotateClockwise(angle)
        else:
            page.rotateCounterClockwise(angle)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open(outFile,'wb') as wFile:
            writer.write(wFile)


pdfFilePath = sys.argv[1]
outFile = sys.argv[2]
if not os.path.isfile(pdfFilePath):
    print(f'The entered string {pdfFilePath} is not a file')
    sys.exit(1)
else:
    rotateClockWise(pdfFilePath,outFile)
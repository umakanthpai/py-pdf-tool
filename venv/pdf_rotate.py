import sys
import os
from pdf_utilities import PDFUtilities

pdfFilePath = sys.argv[1]
outFile = sys.argv[2]
if not os.path.isfile(pdfFilePath):
    print(f'The entered string {pdfFilePath} is not a file')
    sys.exit(1)
else:
    pdfUtil = PDFUtilities()
    pdfUtil.rotateClockWise(pdfFilePath,outFile)
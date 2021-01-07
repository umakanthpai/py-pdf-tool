import sys
import os
from pdf_utilities import PDFUtilities

# Get PDF file paths to merge from arguments
# Last item in the list will be used for output file path
inputPDFs = sys.argv[1:]
outFile = sys.argv[-1]
if not os.path.exists(outFile):
    #print(outFile)
    inputPDFs = inputPDFs[0:len(inputPDFs)-1]
    print(f'Input pdf files: {inputPDFs}')
    print(f'Output merged file is: {outFile}')
    pdfUtil = PDFUtilities()
    pdfUtil.doMerge(inputPDFs,outFile)
else:
    print(f'The output file {outFile} exists. Please delete it or provide a different path')





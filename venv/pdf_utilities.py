import PyPDF2


class PDFUtilities:

    def rotateClockWise(self,pdfFilePath,outFile,direction='clockwise',angle=90):
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

    def doMerge(self,pdf_list, outFilePath="merged.pdf"):
        merger = PyPDF2.PdfFileMerger()
        for aPDF in pdf_list:
            merger.append(aPDF)
        merger.write(outFilePath)

    def doWaterMark(self, pdfToWatermark='sample.pdf', pdfWithWatermark='wtr.pdf',outputfile='pdf_with_watermark.pdf'):
        template = PyPDF2.PdfFileReader(open(pdfToWatermark,'rb'))
        waterMark = PyPDF2.PdfFileReader(open(pdfWithWatermark, 'rb'))
        output = PyPDF2.PdfFileWriter()

        for aPageNum in range(template.getNumPages()):
            aPage = template.getPage(aPageNum)
            aPage.mergePage(waterMark.getPage(0))
            output.addPage(aPage)

            with open(outputfile,'wb') as outFile:
                output.write(outFile)


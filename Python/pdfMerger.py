import PyPDF2

#pdf names
pdfiles=["1.pdf","2,pdf","3.pdf"]
#merge 
merger = PyPDF2.PdfMerger()
#open file
#read file
#and append file
for filename in pdfiles:
    pdfiles = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdfiles)
    merger.append(pdfReader)
#close pdf file
pdfiles.close()
merger.write('merged.pdf')
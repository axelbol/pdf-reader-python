'''
PDF READER
Get and read all the pages from a PDF file
Change PDF path and play with the code!
'''

import PyPDF2
# PRINT ALL PAGES
# read pdf
pdf_object = open('/your/path/file.pdf', 'rb')
# create a pdf reader object
file_pdf = PyPDF2.PdfReader(pdf_object)
# get number of pages
no_pages = len(file_pdf.pages)
# print(no_pages)
# print(type(no_pages))
for no_page in range(no_pages):
  print('Page', no_page+1)
  file_pdf_obj = file_pdf.pages[no_page]
  full_pdf = file_pdf_obj.extract_text()
  print(full_pdf)
  print('*****')

'''
PDF READER
Read a PDF file, split all the words and handle the words as you like
Change PDF path and play with the code!
'''

import PyPDF2
# SPLIT WORDS PDF FILE
def read_and_split_pdf(file_path):
    # With statement ensures that the file is properly closed after use
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        # Get number of pages
        num_pages = len(pdf_reader.pages)
        # Empty string to store all the text extracted from PDF
        all_text = ''

        # Loop to go through page by page
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            # Gets the content of the page and appends it to all_text variable
            # all_text = all_text + page.extract_text()
            all_text += page.extract_text()
            all_text = all_text.lower()

    # All the text from the pages are split into a LIST
    split_words = all_text.split()
    return split_words

# Example usage:
pdf_file_path = '/your/path/file.pdf'
split_words_from_pdf = read_and_split_pdf(pdf_file_path)
print(split_words_from_pdf)

# Display the set elements as a list
print("Python Set:")
for element in split_words_from_pdf:
    print(f"- {element}")

# Word length file
print(f"Words: {len(split_words_from_pdf)}")

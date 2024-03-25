'''
PDF READER
Get unique words of a PDF file using 'set' and count word frequency in a PDF using 'dictionaries'
Change PDF path and play with the code!
Example:
Unique words:
- soccer
- goals
Frequency words
- coach: 2
- field: 3
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

# PDF
pdf_file_path = '/your/path/file.pdf'
split_words_from_pdf = read_and_split_pdf(pdf_file_path)

# Analyze PDF
def analyze_text(pdf):
  words = split_words_from_pdf
  # get unique words
  unique_words = set(pdf)
  # Count words / into a dictionary
  word_frequency = {}

  for word in words:
    if word in word_frequency:
      # word_frequency[word] = word_frequency[word] + 1
      word_frequency[word] += 1
    else:
      word_frequency[word] = 1

  return unique_words, word_frequency

unique_words, word_frequency = analyze_text(split_words_from_pdf)

# Display the set elements as a list
print("Python Set / Unique Words:")
for element in unique_words:
    print(f"- {element}")

# Display the dictionary elements as a list
print("Python Dictionary / Frequency Words:")
for key, value in word_frequency.items():
    print(f"- {key}: {value}")

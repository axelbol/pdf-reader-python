'''
PDF READER
Sets and Dictionaries in Python
Get unique words using 'set' and count word frequency using 'dictionaries' of a single page in a PDF file
Change PDF path and play with the code!
'''

# Sets with one PDF file
import PyPDF2
# creating a pdf file object
file = open('/your/path/file.pdf', 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(file)
# print number of pages of the pdf file
print('Pages: ', len(pdfReader.pages))
# creating a page object
pageObj = pdfReader.pages[0]
# extracting text from page
extract_text = pageObj.extract_text()
# print(extract_text)
def analyze_text(text):
  # split document into words
  words = text.split()
  # get unique words
  unique_words = set(words)
  # Count words / into a dictionary
  word_frequency = {}

  for word in words:
    if word in word_frequency:
      word_frequency[word] += 1
    else:
      word_frequency[word] = 1

  return unique_words, word_frequency

unique_words, word_frequency = analyze_text(extract_text)
# print('Unique words: ', unique_words)
# print('Word frequency: ', word_frequency)

# Display the set elements as a list
print("Python Set:")
for element in unique_words:
    print(f"- {element}")
# Display the dictionary elements as a list
print("Python Dictionary:")
for key, value in word_frequency.items():
    print(f"- {key}: {value}")

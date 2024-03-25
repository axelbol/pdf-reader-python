'''

PDF READER
Argentine President Javier Mieli delivered an opening speech for the 2024 Congress session in early March.

While learning Python, I wanted to analyze his speech and get the most frequently used words in his speech.

In this project I worked with:
- Functions
- For loop
- Pdf Reader
- Sets
- If statement
- Dictionaries
- Word Cloud

Change the PDF path and play with the code!

'''

import PyPDF2
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# SPLIT WORDS MILEI PDF FILE
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

# Read PDF
pdf_file_path = '/home/axel/python/projects/Milei_Pdf/discurso-Milei-congreso-2024.pdf'
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
print("Python Set / Unique words:")
for element in unique_words:
    print(f"- {element}")

# Display the dictionary elements as a list
print("Python Dictionary / Frequency words:")
for key, value in word_frequency.items():
    print(f"- {key}: {value}")

# Get and print spanish stoptwords
print('Spanish stop words:')
print(stopwords.words('spanish'))
print(f"Lengh stopwords: {len(stopwords.words('spanish'))}")

# Add stopwords of my knowledge
stopwords_list = stopwords.words('spanish') + ['paí', 'cada', 'cambio', 'vez', 'salida', 'solo']

# Convert list to a string with words separated by spaces
text = ' '.join(split_words_from_pdf)
print(text)

# Remove stopwords to the 'text'
text_without_stopwords = ' '.join([x for x in text.strip().lower().split(' ') if x not in stopwords_list and len(x) > 3])
print(text_without_stopwords)

# Use WordCloud to get the image of the most used words in the speech
wc = WordCloud(background_color = 'white', height=800, width=1000)
wc.generate(text_without_stopwords)

plt.axis('off')
plt.imshow(wc, interpolation='bilinear')
# plt.show()
# Save the image
wc.to_file("/your/path/milei_speech_wc.png")

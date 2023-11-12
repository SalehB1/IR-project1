import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize
from nltk.stem import PorterStemmer

# Load data
df = pd.read_csv("plot_summaries.txt", delimiter="\t", names=["id", "text"])

# NLTK text processing

nltk.download('punkt')
nltk.download('stopwords')
punkt_tokenizer = PunktSentenceTokenizer()
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))


# Function to normalize, tokenize, remove stopwords, and stem the text
def process_text(text):
    words = word_tokenize(text)
    remove_punctuation = [word for word in words if word.isalpha()]
    words = [word for word in remove_punctuation if word not in stop_words]  # Remove stopwords
    stemmed_words = [stemmer.stem(words) for words in words]

    return ','.join(stemmed_words)


# Apply the function to the 'text' column
df['processed_text'] = df['text'].apply(process_text)

# Save the new DataFrame to an Excel file
df.to_csv('processed_data-eng-final.csv', index=False)

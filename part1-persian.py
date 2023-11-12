import hazm
import pandas as pd
from hazm import Normalizer, Stemmer, word_tokenize, stopwords_list

df = pd.read_excel('final_books.xlsx')
normalizer = Normalizer()
# stemmer = Stemmer()
stopwords = stopwords_list()


# Function to merge all columns
def merge_columns(row):
    merged = ' '.join(row.astype(str))  # Merge all columns
    return merged


# Apply the function to each row
df['merged'] = df.apply(merge_columns, axis=1)

# Create a new DataFrame to store the input data and tokenized text
new_df = pd.DataFrame(columns=['input', 'tokenized_text'])

for index, row in df.iterrows():
    for column_name, data in row.items():
        if column_name == 'merged':
            normalize_text = normalizer.normalize(data)
            words = word_tokenize(normalize_text)
            words = [word for word in words if word not in stopwords]  # Remove stopwords
            # stemmed_words = [stemmer.stem(word) for word in words]  # Apply stemming
            tokenize_text = ' '.join(words)

            # Append the input data and tokenized text to the new DataFrame
            new_df = new_df._append({'input': data, 'tokenized_text': tokenize_text}, ignore_index=True)

# Save the new DataFrame to an Excel file
new_df.to_csv('without stop word.xlsx', index=False)

import os
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import nltk

nltk.download('punkt')
nltk.download('stopwords')


def main():
    input_directory = 'Input_Directory/'
    output_directory = 'Output_Directory/'
    preprocess_dataset(input_directory, output_directory)


# All text processing
def process_text(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        file_content = file.read()

    lowercase_text = Lowercase(file_content)
    tokenization = Tokenization(lowercase_text)
    removeStopwords = Remove_stopwords(tokenization)
    removePunctuation = Remove_punctuation(removeStopwords)
    removeBlankspaces = Remove_blankspaces(removePunctuation)
    tokens = Tokenization(removeBlankspaces)

    with open(output_file_path, 'w') as output_file:
        output_file.write(' '.join(tokens))


# Getting path of input and output directory
def preprocess_dataset(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, filename)
            process_text(input_file_path, output_file_path)


def Lowercase(text):
    return text.lower()


def Remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))


def Tokenization(text):
    return word_tokenize(text)


def Remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    filtered_text = [word for word in text if word.lower() not in stop_words]
    return ' '.join(filtered_text)


def Remove_blankspaces(text):
    tokens = text.split()
    non_empty_tokens = [token for token in tokens if token.strip()]
    return ' '.join(non_empty_tokens)


if __name__ == "__main__":
    main()

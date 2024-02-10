import os
import string
from nltk import word_tokenize
from nltk.corpus import stopwords


def main():
    input_directory = 'Input_Directory/'
    output_directory = '5_sampleFile/'
    preprocess_dataset(input_directory, output_directory)


def preprocess_dataset(input_directory, output_directory):
    Processed_File = 0
    SampleFileCount = 5

    for filename in os.listdir(input_directory):
        if Processed_File >= SampleFileCount:
            break

        if filename.endswith(".txt"):
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, filename)
            process_text(input_file_path, output_file_path, Processed_File)

            Processed_File += 1


def process_text(input_file_path, output_file_path, count):
    with open(input_file_path, 'r') as file:
        file_content = file.read()

    print('file', f"{count}:{file_content}")

    lowercase_text = Lowercase(file_content)
    print('file', f"{count}(lowercase):{lowercase_text}")

    tokenization = Tokenization(lowercase_text)
    print('file', f"{count}(tokenization):{tokenization}")

    removeStopwords = Remove_stopwords(tokenization)
    print('file', f"{count}(Stopwords):{removeStopwords}")

    removePunctuation = Remove_punctuation(removeStopwords)
    print('file', f"{count}(Punctuation):{removePunctuation}")

    removeBlankspaces = Remove_blankspaces(removePunctuation)
    print('file', f"{count}(Blankspaces):{removeBlankspaces}")

    tokens = Tokenization(removeBlankspaces)

    with open(output_file_path, 'w') as output_file:
        output_file.write(' '.join(tokens))


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

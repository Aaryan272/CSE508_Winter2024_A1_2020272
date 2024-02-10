import os
import pickle
from nltk import word_tokenize

OUTPUT_DIRECTORY = 'Output_Directory/'


def main():
    positional_index = Access_Directory(OUTPUT_DIRECTORY)
    save_positional_index(positional_index)
    print_positional_index()


def Access_Directory(output_directory):
    positional_index = {}

    for filename in os.listdir(output_directory):
        if filename.endswith(".txt"):
            document_id = filename
            output_file_path = os.path.join(output_directory, filename)

            with open(output_file_path, 'r') as file:
                file_content = file.read()

            build_positional_index(file_content, document_id, positional_index)
    return positional_index


def build_positional_index(file_content, document_id, positional_index):
    terms = word_tokenize(file_content)
    # unique terms
    unique_terms = list(set(terms))

    # giving unique terms with repetition as well
    terms_positions = {
        term:
            [i for i, j in enumerate(terms) if j == term]
        for term in unique_terms
    }
    update_positional_index(positional_index, terms_positions, document_id)
    return positional_index


def update_positional_index(positional_index, terms_positions, document_id):
    for term, position in terms_positions.items():
        if term not in positional_index:
            positional_index[term] = {document_id: position}
        else:
            if document_id not in positional_index[term]:
                positional_index[term][document_id] = position
            else:
                positional_index[term][document_id].extend(position)
    return positional_index


def save_positional_index(positional_index):
    filename = 'Positional_index.pkl'
    with open(filename, 'wb') as file:
        pickle.dump(positional_index, file)


def print_positional_index():
    filename = 'Positional_index.pkl'
    with open(filename, 'rb') as file:
        positional_index = pickle.load(file)
    for term, postings in positional_index.items():
        print(f"{term}:{postings}")


if __name__ == "__main__":
    main()

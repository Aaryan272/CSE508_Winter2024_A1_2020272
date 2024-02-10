import os
import pickle

OUTPUT_DIRECTORY = 'Output_Directory/'


def main():
    inverted_index = build_inverted_index(OUTPUT_DIRECTORY)
    save_UII(inverted_index)
    load_UII(inverted_index)

    print_loaded_index(inverted_index)


def build_inverted_index(output_directory):
    inverted_index = {}

    for filename in os.listdir(output_directory):
        if filename.endswith(".txt"):
            document_id = filename
            output_file_path = os.path.join(output_directory, filename)

            with open(output_file_path, 'r') as file:
                file_content = file.read()

            terms = file_content.split()
            update_inverted_index(inverted_index, terms, document_id)

    return inverted_index


def update_inverted_index(inverted_index, terms, document_id):
    for term in terms:
        if term not in inverted_index:
            inverted_index[term] = [document_id]
        else:
            if document_id not in inverted_index[term]:
                inverted_index[term].append(document_id)


def save_UII(inverted_index):
    filename = 'Unigram_inverted_index.pkl'
    with open(filename, 'wb') as file:
        pickle.dump(inverted_index, file)
    return inverted_index


def load_UII(inverted_index):
    filename = 'Unigram_inverted_index.pkl'
    with open(filename, 'rb') as file:
        inverted_index = pickle.load(file)
    return inverted_index


def print_loaded_index(loaded_index):
    for term, filenames in loaded_index.items():
        print(f"{term}: {filenames}")


if __name__ == "__main__":
    main()

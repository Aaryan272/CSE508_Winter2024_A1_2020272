import pickle


def main():
    filename = 'Unigram_inverted_index.pkl'
    with open(filename, 'rb') as file:
        file_content = pickle.load(file)
    T1 = input()
    T2 = input()
    if isinstance(T1, str) and isinstance(T2, str):
        AND = AND_operation(T1, T2, file_content)
        OR = OR_operation(T1, T2, file_content)
        AND_NOT = AND_NOT_operation(T1, T2, file_content)
        OR_NOT = OR_NOT_operation(T1, T2, file_content)

        print(f"AND operation:{AND}")
        print(f"OR operation:{OR}")
        print(f"AND NOT operation:{AND_NOT}")
        print(f"OR NOT operation:{OR_NOT}")


def print_loaded_index(loaded_index):
    for term, filenames in loaded_index.items():
        print(f"{term}: {filenames}")


def AND_operation(T1, T2, UII):
    if T1 in UII and T2 in UII:
        return set(UII[T1]).intersection(UII[T2])
    else:
        return set()


def OR_operation(T1, T2, UII):
    if T1 in UII and T2 in UII:
        return set(set(UII[T1]).union(UII[T2]))
    elif T1 in UII:
        return set(UII[T1])
    elif T2 in UII:
        return set(UII[T2])
    else:
        return set()


def AND_NOT_operation(T1, T2, UII):
    if T1 in UII and T2 in UII:
        return set(UII[T1]).difference(UII[T2])
    elif T1 in UII:
        return set(UII[T1])
    else:
        return set()


def OR_NOT_operation(T1, T2, UII):
    if T1 in UII and T2 in UII:
        ALL_T = set(UII.keys())
        T1_1 = set(UII[T1])
        T2_2 = set(UII[T2])
        return ALL_T.difference(T2_2).union(T1_1)
    elif T1 in UII:
        return set(UII[T1])
    else:
        return set()


if __name__ == "__main__":
    main()

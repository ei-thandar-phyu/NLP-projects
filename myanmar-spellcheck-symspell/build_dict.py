import argparse

def count_unigram(in_f, out_f, dict_f=None):
    count = dict()

    # Optionally add words from dictionary file
    if dict_f:
        with open(dict_f, 'r', encoding="utf-8") as f:
            for line in f:
                word = line.strip()
                count[word] = count.get(word, 0) + 1

    with open(in_f, 'r', encoding="utf-8") as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                count[word] = count.get(word, 0) + 1

    sorted_dict = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

    with open(out_f, "w", encoding="utf-8") as f:
        for k, v in sorted_dict.items():
            f.write(f"{k} {v}\n")


def count_bigram(in_f, out_f):
    count = dict()
    with open(in_f, 'r', encoding="utf-8") as f:
        for line in f:
            words = line.strip().split()
            for i in range(len(words) - 1):
                bigram_word = f"{words[i]} {words[i+1]}"
                count[bigram_word] = count.get(bigram_word, 0) + 1

    sorted_dict = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

    with open(out_f, "w", encoding="utf-8") as f:
        for k, v in sorted_dict.items():
            f.write(f"{k} {v}\n")


def main():
    parser = argparse.ArgumentParser(description="Frequency dictionaries for SymSpell")
    parser.add_argument("-i", "--input_file", required=True, help="Input Filename")
    parser.add_argument("-o", "--output_file", required=True, help="Output Filename")
    parser.add_argument("-t", "--dict_type", required=True, choices=["unigram", "bigram"], help="Type of dictionary: unigram or bigram")
    parser.add_argument("-d", "--dict_file", required=False, help="Optional: List of known Myanmar words (to prioritize in unigram dictionary)")

    args = parser.parse_args()

    if args.dict_type == "unigram":
        count_unigram(args.input_file, args.output_file, args.dict_file)
    elif args.dict_type == "bigram":
        count_bigram(args.input_file, args.output_file)


if __name__ == "__main__":
    main()

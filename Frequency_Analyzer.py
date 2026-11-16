filename = "sample.txt"  # Replace with your actual filename

try:
    with open(filename, "r") as f:
        text = f.read()

        # lowecase everting and split into raws
        raw_words = text.lower().split()

        word_counts = {}

        for word in raw_words:
            # cleaning the texts
            clean_word = word.strip(".,!?:;\"'()")

            if clean_word:
                word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

        print(f"Total unique words:{len(word_counts)}")
        print("word frequency:", word_counts)

        # finding the most frequent word

        if word_counts:
            most_common_word = max(word_counts, key=word_counts.get)
            highest_count = word_counts[most_common_word]
            print(
                f"The most frequent word is:'{most_common_word}' with a count of {highest_count}"
            )

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

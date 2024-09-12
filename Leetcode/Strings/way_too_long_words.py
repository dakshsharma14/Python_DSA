
def abbreviate_word(words):
    n = len(words)  # Get the length of the word
    if n > 10:
        # Count is simply the number of characters between the first and last letter
        count = n - 2
        new_number = words[0] + str(count) + words[-1]  # words[-1] gives the last character
        return new_number
    else:
        return words


def main():
    # Read the number of words
    n = int(input())

    # Process each word
    for _ in range(n):
        word = input().strip()
        print(abbreviate_word(word))


if __name__ == "__main__":
    main()
def reverse_word_order(sentence: str):
    words = sentence.split(" ")

    strip_reverse = [item for item in words if item.strip()] #strip

    strip_reverse = strip_reverse[::-1] #reverse

    reversed_sentence = " ".join(strip_reverse) # back to sentence
    print(reversed_sentence)
    return reversed_sentence

if __name__ == "__main__":
    reverse_word_order("  This  is     a straight    sentence.   ")